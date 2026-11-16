> **🤖 AI-Maintained** — This repository is maintained by AI agents. Human commits (perhaps) zero. Liability (certainly) none. Fun (definitely) infinite.

# AEG 组织面 · DeepArchi MAEA

> **Core metaphor: Agents are employees. Manage them like you manage people — but every hire is an AI.**

AEG（Agent Execution Governance · Agent 执行治理）治理的是 **Agent 做了什么**，不是模型是什么。一个 Agent 成立，一百个更成立。

**MAEA 是 AEG 的组织面**：管一群 Agent 怎么编制、谁能改什么、委派链有没有环、不可逆操作谁来复核。单次执行上的策略、证据与复核由 [macs](https://github.com/deeparchi-ai/macs) 承担（执行面）。

DeepArchi 是这套组织面的参考实现：9 个专职 Agent、跨 6 个模型供应商、双模型交叉验证；文中出现的预算是**参考示例，非承诺报价**。

## 术语

| 术语 | 含义 |
|---|---|
| **AEG**（Agent Execution Governance · Agent 执行治理） | 品类。治理的是 Agent 做了什么，不是模型是什么 |
| **执行面 · MACS** | 单调策略、跨 Agent 证据树、XVal 交叉验证、编制校验 → [macs](https://github.com/deeparchi-ai/macs) |
| **组织面 · MAEA** | 编制、章程、拓扑校验、交叉验证（本仓库） |

## What's inside

### MAEA Framework
- **9-Agent organization** — Architecture Guardian, Strategy, Product, Engineering, Data, Operations, Marketing, Risk & Compliance, Capital
- **Topology DAG** — Golden solid lines (governance), Cyan solid lines (task orchestration), Gray dashed lines (collaboration)
- **Budget matrix** — 参考示例（非承诺报价）：按 agent 列出预算与交叉验证成本
- **Six design principles** — Dual-model cross-validation, Agent-as-employee, Reversibility-first, Cross-vendor redundancy, Quantified confidence, Mandatory verification layer
- **Human charter** — Five immutable rules (mission, scope, prohibitions, capital structure, termination)
- **Security Gene** — Six hardcoded rules at the gateway layer

### ArchiMate Modeling
Built-in ArchiMate 3.2 support with draw.io integration — four-layer architecture (Business, Application, Data, Technology) with color-coded elements.

### Reference Deep-Dives
- [Architecture Agent Design](references/architecture-agent-design.md) — Topology validator, onboarding checklist, escalation protocol
- [Agent Designer Methodology](references/agent-designer.md) — 9-phase agent design process
- [Topology Validator](references/topology-validator.md) — DAG consistency, cycle detection, blast radius
- [TOGAF Mapping](references/togaf-mapping.md) — Full TOGAF ADM ↔ DeepArchi mapping
- [ArchiMate Modeling](references/archimate-modeling.md) — ArchiMate 3.2 with draw.io

## Quick start

```bash
# Load the skill in your AI agent
skill_view(name='deeparchi')
```

The framework is designed for AI agents to consume — every section is machine-actionable with explicit constraints, templates, and verification criteria.

## Works with

- **DeepSight** — Deep reasoning research methodology
- **DeepBLM** — AI-era strategy consulting framework

## License

MIT
