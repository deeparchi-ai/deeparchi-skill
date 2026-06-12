# TOGAF → DeepArchi 多Agent企业架构框架 (MAEA) 映射参考

> 来源：kuangmi-bit/deeparchi-skill 提取 + TOGAF 10th Edition 知识整合
> 用途：为 DeepArchi 多Agent企业架构框架 (MAEA)提供 TOGAF 企业架构方法论的体系支撑

---

## 一、TOGAF ADM 阶段 → DeepArchi 多Agent企业架构框架 (MAEA) 五阶段映射

```
TOGAF ADM Phase                    DeepArchi 多Agent企业架构框架 (MAEA) 阶段
──────────────────────────────────────────────────────
Preliminary Phase                  创立期
  (架构原则、治理框架)              (人类章程、资本注入、安全边界)

Phase A: Architecture Vision       创立期
  (愿景、范围、利益相关者)          (使命定义、业务范围、边界划定)

Phase B: Business Architecture     架构设计期
  (业务能力、组织架构)              (岗位图谱、Agent角色对标人类岗位)

Phase C: Information Systems       架构设计期
  (数据架构 + 应用架构)             (模型选型矩阵、Agent规格书、I/O Schema)

Phase D: Technology Architecture   架构设计期
  (技术基础设施)                     (阿里云资源配置、A2A总线协议)

Phase E: Opportunities & Solutions 架构设计期
  (实施方案、迁移规划)              (预算矩阵、成本基线)

Phase F: Migration Planning        招聘组建期
  (过渡架构、实施路线图)            (6天启动计划、Agent孵化、影子测试)

Phase G: Implementation Governance 运营期
  (实施监督、合规)                  (SLA追踪、绩效浮动、全成本核算)

Phase H: Architecture Change       进化期
  (变更管理)                        (模型升级、架构重构、代际更替)

Requirements Management            贯穿全生命周期
  (需求管理)                        (A2A总线承载的Agent间请求)
```

---

## 二、TOGAF 四大架构域 → DeepArchi Agent 层映射

```
TOGAF Domain          DeepArchi 多Agent企业架构框架 (MAEA) 对应
────────────────────────────────────────────
Business Architecture → 战略Agent + 产品Agent
  (业务能力、流程、组织)   (战略分析 + 需求结构化)

Data Architecture     → 数据Agent
  (数据模型、信息流)       (建模 + 查询 + 因果推断)

Application Architecture → 工程Agent + 运营Agent
  (应用组合、服务)         (代码生成 + 流程编排)

Technology Architecture  → 阿里云基础设施 + A2A总线
  (平台、网络、硬件)       (ACK/RDS/OSS/DashVector)
```

---

## 三、TOGAF 架构治理 → DeepArchi 审批链

```
TOGAF 治理概念              DeepArchi 多Agent企业架构框架 (MAEA) 对应
─────────────────────────────────────────────────
Architecture Board          架构守护Agent (DEEPAR-000)
  (架构合规审查)              (拓扑兼容性审查 + 原则仲裁)

Architecture Contract       人类章程 §1-§5
  (架构契约)                  (五条不可修改的硬约束)

Architecture Compliance     风控Agent + 架构Agent 安全校验
  Review (合规审查)            (安全Gene注入 + 安全边界闭环校验)

Dispensation (豁免)         人类章程层审批
  (打破架构原则的例外)         (安全Gene修改、章程修改——仅人类可批)

Architecture Repository     DashVector 知识湖
  (架构资产库)                 (Agent退役知识归档 + 会话记录)

Architecture Capability     运营Agent + AI创始人Agent
  (架构能力建设)              (流程编排 + 能力边界探索)
```

---

## 四、TOGAF 交付物 → DeepArchi 制品

```
TOGAF Deliverable              DeepArchi Artifact
─────────────────────────────────────────────────────
Architecture Vision            人类章程 §1 使命声明
Architecture Definition Doc    Agent 规格书 (JD, 12字段)
Architecture Requirements Spec I/O Schema (Input/Output JSON Schema)
Architecture Roadmap           6天启动计划
Migration Plan                 Agent退役流程 (6步)
Implementation Governance     运营节律 (实时/日/周/月/季)
Architecture Contract          安全Gene (6条硬编码规则)
Compliance Assessment          Mutual Audit + 交叉验证协议
Change Request                 A2A协议版本的拓扑变更请求
Solution Building Blocks       Agent System Prompt + 模型选型
```

---

## 五、TOGAF Architecture Content Framework 映射

```
TOGAF 内容元模型               DeepArchi 多Agent企业架构框架 (MAEA) 对应
─────────────────────────────────────────────────────
Capability (能力)              Agent能力标准 (推理/知识/工具，10分制)
Function (功能)                Agent职责清单 (做什么 ✅)
Organization Unit (组织单元)   Agent序列 (战略/架构/产品/工程...)
Role (角色)                    对标人类角色 (CEO/CTO/COO/Senior Dev...)
Actor (参与者)                 Agent实例 (DEEPAR-000 ~ 008)
Business Service (业务服务)    A2A总线上的服务调用
Application Component (应用)   Agent运行实例 (ACK Serverless容器)
Technology Component (技术)    阿里云基础设施 (ECS/RDS/OSS...)
Data Entity (数据实体)         DashVector命名空间 + OSS工作目录
```

---

## 六、TOGAF Enterprise Continuum → DeepArchi 能力演进

```
TOGAF Continuum               DeepArchi 多Agent企业架构框架 (MAEA) 对应
─────────────────────────────────────────────────────
Foundation Architecture       人类章程 (不可变的宪法级架构)
  (通用基础)

Common Systems Architecture   模型选型矩阵 (跨供应商的通用模型层)
  (通用系统)

Industry Architecture         BIAN/FinTech 行业框架
  (行业特定)                   (如后续引入BIAN，映射到产品Agent)

Organization-Specific         Agent画像 + System Prompt
  Architecture                 (每个Agent的个性化设计)
  (组织特定)
```

---

## 七、TOGAF 原则 → DeepArchi 原则对照

```
TOGAF 架构原则                 DeepArchi 原则
─────────────────────────────────────────────────────
Primacy of Principles          §1-§5 不可修改
  (原则至上)

Business Continuity            淘汰线 + 退役流程
  (业务连续性)

Data is an Asset               DashVector永久存储 + 知识传承
  (数据是资产)

Technology Independence        跨供应商模型选型 + 备选降级
  (技术独立性)

Compliance with Law            风控Agent + 安全Gene
  (合规)
```

---

## 八、关键设计洞察

### ADM 循环 → MAEA 循环

TOGAF ADM 是一个**迭代循环**（每个Phase可以回到前面），而 DeepArchi 多Agent企业架构框架 (MAEA) 是**线性推进 + 内部循环**。这反映了两者的本质差异：

- **TOGAF** = 人类组织的架构方法，需要反复协商
- **DeepArchi 多Agent企业架构框架 (MAEA)** = Agent集群的运行框架，Agent可以快速迭代（影子测试→上线），但结构性变更（拓扑/章程）是单向不可逆的

### 治理的自动化程度差异

TOGAF 的治理依赖**人类 Architecture Board**，而 DeepArchi 将治理分为三级：
- **L1 自动化**：架构Agent自主裁决routine级变更
- **L2 半自动**：架构Agent建议 + 人类审批
- **L3 纯人类**：章程修改、安全Gene修改

这是 TOGAF 思想在AI时代的延伸——用Agent替代人类执行routine治理，只在关键决策点保留人类。

### 从"文档驱动"到"Agent驱动"

TOGAF 是文档驱动（每个Phase产出文档），DeepArchi 是Agent驱动：
- 架构定义文档 → Agent规格书（不仅描述，还能执行）
- 合规审查 → 风控Agent 7×24自动审计
- 变更管理 → 架构Agent的拓扑兼容性自动检查
