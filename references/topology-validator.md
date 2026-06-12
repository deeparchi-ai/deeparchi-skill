---
name: topology-validator
description: "DeepArchi 多Agent企业架构框架 (MAEA) DAG 拓扑验证工具 — 用于校验多Agent组织拓扑图的一致性。执行6步确定性算法：循环依赖检测(DFS)、孤点检测、爆炸半径计算(BFS)、安全边界校验、新Agent入网审查(8项清单)。当需要审查Agent入网/退役/拓扑变更/新通信路径时使用。由架构守护Agent (DEEPAR-000) 调用。"
---

# Topology Validator · DeepArchi 多Agent企业架构框架 (MAEA)

> 执行者：架构守护Agent (DEEPAR-000) · 调用时机：任何拓扑变更提交前

---

## 输入格式

```json
{
  "current_dag": {
    "nodes": ["DEEPAR-000", "DEEPAR-001", ...],
    "edges": [["DEEPAR-000", "DEEPAR-001"], ...]
  },
  "proposed_change": {
    "type": "add_node|remove_node|add_edge|remove_edge|replace_model",
    "target": "DEEPAR-XXX",
    "details": {}
  }
}
```

---

## 6步验证算法

```
Step 1 — 快照冻结
  dag = 当前DAG邻接表（节点列表 + 有向边列表）

Step 2 — 变更模拟
  将 proposed_change 应用到 dag → dag'（不修改原始dag）

Step 3 — 循环检测 (DFS)
  FOR each node in dag':
    从 node 出发做 DFS，记录访问路径
    IF 访问到已在路径中的节点 → REJECT: "循环依赖: [path]"
  所有节点通过 → PASS

Step 4 — 孤点检测
  FOR each node in dag'（架构Agent除外）:
    IF 入度 + 出度 = 0 → WARN: "孤立节点: [node]"

Step 5 — 爆炸半径 (BFS)
  从变更节点出发做 BFS，深度 ≤ 3
  affected_count = 受影响节点数
  IF affected_count ≥ 5 → risk = "critical"
  ELIF affected_count ≥ 3 → risk = "elevated"
  ELSE → risk = "routine"

Step 6 — 安全边界
  IF 新增通信路径涉及 L1 Agent → WARN: "L1路径变更需特别论证"
  IF 存在 L2→L1 上行数据流 → REJECT: "安全边界违反: L2→L1上行"
```

---

## 新Agent入网清单（8项）

仅当 `proposed_change.type = "add_node"` 时执行：

```
□ 1. 拓扑兼容性   — 不产生循环依赖？职责重叠 < 50%？
□ 2. 安全等级赋值 — L1/L2/L3 正确标注？L1 需额外论证
□ 3. I/O Schema   — 上游输出是该Agent输入的超集？
□ 4. 模型选型     — 符合选型矩阵？有跨供应商备选？
□ 5. 安全Gene     — 6条规则全部约束？Gateway校验已配置？
□ 6. 预算可行性   — 新Agent + 现有总计 ≤ 120% 月预算？
□ 7. 影子测试计划 — 主观Agent ≥ 14天 / 客观Agent ≥ 7天
□ 8. 退役预案     — 触发条件 / 知识归档 / 下游重路由已定义

判定：[0预警 → 批准] [1-2预警 → 有条件批准] [≥3预警 → 驳回]
```

---

## 输出格式

```json
{
  "validation_id": "TOPO-YYYYMMDD-NNN",
  "timestamp": "ISO 8601",
  "dag_before": {"nodes": 9, "edges": 12},
  "dag_after":  {"nodes": 10, "edges": 13},
  "steps": {
    "cycle_check":    {"status": "pass|reject", "detail": ""},
    "orphan_check":   {"status": "pass|warn",   "orphans": []},
    "blast_radius":   {"affected": [], "count": 2, "risk": "routine|elevated|critical"},
    "security_check": {"status": "pass|warn|reject", "detail": ""}
  },
  "onboarding_checklist": {"passed": 8, "warnings": [], "result": "approve|conditional|reject"},
  "final_verdict": "approve|approve_with_conditions|reject",
  "conditions": [],
  "escalation_required": false,
  "risk_level": "routine"
}
```

---

## 裁决规则

| 条件 | 裁决 |
|------|------|
| 所有步骤 PASS，无 WARN | `approve` |
| 有 WARN，无 REJECT | `approve_with_conditions` + 列出条件 |
| 任一步骤 REJECT | `reject` + 说明原因 |
| risk ≥ elevated | `escalation_required: true` → 转四级升级协议 |

---

## 拓扑约束速查

| 约束 | 规则 |
|------|------|
| 无循环依赖 | DFS 检测，禁止任何环 |
| 单根节点 | 仅人类章程可为根（无入边） |
| 深度限制 | 最大深度 ≤ 4 |
| L1 隔离 | L1 Agent 只与架构Agent直连 |
| 横向禁止 | 同级 Agent 不得绕过架构Agent 直连 |

> 完整 DAG 邻接表和组织拓扑图见：`../../../designs/organization-topology.md`
