---
name: deeparchi
version: 1.3.0
description: Create ArchiMate 3.2 compliant enterprise architecture diagrams using draw.io. Supports four-layer architecture (Business, Application, Data, Technology) with color-coded element types. Integrates with archimate, togaf, ddd, bian, bpmn, it4it, drawio-skill skills for comprehensive enterprise architecture modeling.
author: DeepArchi
license: MIT
keywords:
  - archimate
  - enterprise-architecture
  - drawio
  - togaf
  - bian
  - ddd
  - bpmn
  - it4it
  - architecture-modeling
  - deeparchi
  - data-architecture
integrates:
  - archimate
  - togaf
  - ddd
  - bian
  - bpmn
  - it4it
  - drawio-skill
---

# DeepArchi Skill - ArchiMate 架构建模

## 概述

DeepArchi Skill 是一个专门用于创建符合 ArchiMate 3.2 标准的企业架构图的技能。该技能集成了 draw.io 工具，帮助架构师快速创建标准化的企业架构视图。

## 集成技能

DeepArchi 可与以下技能协同工作：

| 技能 | 用途 | 协作方式 |
|------|------|---------|
| **archimate** | ArchiMate 3.2 规范 | 元素类型、关系矩阵、视角选择参考 |
| **togaf** | 架构开发方法 | ADM 交付物可视化 |
| **ddd** | 领域驱动设计 | 领域模型到应用架构映射 |
| **bian** | 银行业架构 | BIAN 服务域到业务层映射 |
| **bpmn** | 流程建模 | 流程到业务过程映射 |
| **it4it** | IT 服务管理 | 价值流到技术层映射 |
| **drawio-skill** | 图表绘制工具 | 提供 draw.io 图表创建和编辑能力 |

## 何时使用

当用户需要：
- 创建符合 ArchiMate 标准的企业架构图
- 使用 draw.io 绘制架构视图
- 生成业务架构、应用架构、数据架构、技术架构等视图
- 创建架构资产的可视化表达
- 遵循 TOGAF、ArchiMate 或 BIAN 框架的架构设计
- 结合 DDD、BPMN、IT4IT 等方法论进行架构设计

## 快速开始

1. 参考 `README.md` 了解四层架构和颜色规范
2. 查看 `assets/archimate-color-palette.json` 获取完整的颜色和样式定义
3. 使用 `assets/digital-bank-archimate.drawio` 作为模板参考
4. 参考 `references/drawio-archimate-tutorial.md` 学习 Draw.io 操作

## 核心功能

- **四层架构支持**：Business、Application、Data、Technology
- **颜色渐变规范**：每层使用深浅渐变区分元素类型
- **Draw.io XML 样式**：正确的 `mxgraph.archimate3.application` 样式
- **BIAN 框架集成**：支持银行业标准服务域定义
- **多页面视图**：Business/Application/Data/Technology/CrossLayer/Legend

## 颜色速查

```
Business Layer (黄色系):
  Role: #FFF8DC | Process: #FFE699 | Service: #FFD54F | Object: #F4B942

Application Layer (绿色系):
  Service: #E8F5E9 | Component: #66BB6A

Data Layer (蓝色系):
  Object: #BBDEFB | Service: #64B5F6 | Database: #1976D2

Technology Layer (绿色系):
  Service: #DCEDC8 | SysSw: #AED581 | Node: #7CB342
```

## 样式模板

```xml
<!-- 通用样式格式 -->
shape=mxgraph.archimate3.application;appType=<类型>;archiType=<形状>;fillColor=<颜色>;strokeColor=#666666;

<!-- appType 可选值: role, proc, serv, passive, comp, node, sysSw, actor -->
<!-- archiType 可选值: square (直角), rounded (圆角) -->
```

## 资源文件

- `README.md` - 完整技能文档
- `EXAMPLES.md` - 使用示例
- `assets/archimate-color-palette.json` - 颜色和样式定义
- `assets/digital-bank-archimate.drawio` - 数字银行架构示例
- `references/archimate-relationships-guide.md` - 关系使用指南
- `references/drawio-archimate-tutorial.md` - Draw.io 教程
- `scripts/validate-archimate.js` - 验证脚本

## 相关链接

- [ArchiMate 官方网站](https://www.opengroup.org/archimate)
- [Draw.io 官方网站](https://app.diagrams.net/)
- [TOGAF 官方网站](https://www.opengroup.org/togaf)
- [BIAN 银行业架构网络](https://bian.org/)
- [IT4IT 参考架构](https://www.opengroup.org/it4it)
- [DeepArchi 架构管理平台](https://www.deeparchi.com.cn)

## 关联技能

- `archimate` - ArchiMate 3.2 建模语言规范 (元素/关系/视角)
- `togaf` - TOGAF 企业架构框架
- `ddd` - 领域驱动设计
- `bian` - 银行业架构网络
- `bpmn` - 业务流程建模
- `it4it` - IT 管理参考架构
- `drawio-skill` - Draw.io 图表绘制工具
