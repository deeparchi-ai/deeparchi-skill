# DeepArchi Skill - ArchiMate 架构建模

## 概述

DeepArchi Skill 是一个专门用于创建符合 ArchiMate 3.2 标准的企业架构图的技能。该技能集成了 draw.io 工具，帮助架构师快速创建标准化的企业架构视图。

## 何时使用

当用户需要：
- 创建符合 ArchiMate 标准的企业架构图
- 使用 draw.io 绘制架构视图
- 生成业务架构、应用架构、数据架构、技术架构等视图
- 创建架构资产的可视化表达
- 遵循 TOGAF、ArchiMate 或 BIAN 框架的架构设计

## 集成技能 (Integrated Skills)

DeepArchi 与以下技能协同工作，提供完整的企业架构解决方案：

### 调用方式

在需要特定领域支持时，可以调用相关技能：

| 技能 | 调用场景 | 协同方式 |
|------|---------|---------|
| **archimate** | ArchiMate 3.2 规范查询 | 提供元素类型、关系矩阵、视角选择参考 |
| **togaf** | 架构开发方法、治理流程 | 提供 ADM 阶段交付物的可视化 |
| **ddd** | 领域建模、限界上下文设计 | 将领域模型映射到应用层架构 |
| **bian** | 银行业服务域设计 | 将 BIAN 服务域映射到业务层 |
| **bpmn** | 业务流程建模 | 将流程图转换为业务过程视图 |
| **it4it** | IT 服务管理架构 | 将 IT4IT 价值流映射到技术层 |
| **drawio-skill** | 图表绘制和编辑 | 提供 draw.io 图表创建、编辑和导出能力 |

### 技能协作示例

#### 0. ArchiMate + DeepArchi 协作

```
用户请求: "创建一个应用协作视图"

步骤:
1. 调用 archimate skill 查询:
   - 应用协作视角 (Application Cooperation Viewpoint) 包含的元素
   - 有效的关系类型 (Serving, Flow, Triggering)
   - 关系方向约定
2. 使用 deeparchi 创建视图:
   - Application Component (绿色组件)
   - Application Interface (接口)
   - Application Service (浅绿服务)
   - Data Object (蓝色数据对象)
3. 按 archimate 关系矩阵添加连接
```

#### 1. TOGAF + DeepArchi 协作

```
用户请求: "基于 TOGAF ADM 设计银行数字化转型架构"

步骤:
1. 调用 togaf skill 获取 ADM 阶段和交付物定义
2. 使用 deeparchi 创建各阶段的架构视图:
   - Phase B (业务架构) → Business View
   - Phase C (信息系统架构) → Application View + Data View
   - Phase D (技术架构) → Technology View
3. 创建 Cross Layer View 展示架构全景
```

#### 2. DDD + DeepArchi 协作

```
用户请求: "设计电商系统的领域架构"

步骤:
1. 调用 ddd skill 进行领域分析:
   - 识别核心域、支撑域、通用域
   - 定义限界上下文和上下文映射
2. 使用 deeparchi 可视化领域架构:
   - 限界上下文 → Application Component
   - 聚合根 → Data Object
   - 领域服务 → Application Service
   - 领域事件 → Business Object
```

#### 3. BIAN + DeepArchi 协作

```
用户请求: "设计零售银行核心系统架构"

步骤:
1. 调用 bian skill 获取服务域定义:
   - 识别相关 Business Areas
   - 选择适用的 Service Domains
   - 获取 API 设计规范
2. 使用 deeparchi 创建架构视图:
   - Service Domain → Business Service (黄色)
   - API Endpoint → Application Service (浅绿)
   - Data Entity → Data Object (蓝色)
```

#### 4. BPMN + DeepArchi 协作

```
用户请求: "设计贷款审批流程的架构"

步骤:
1. 调用 bpmn skill 设计业务流程:
   - 创建贷款申请流程图
   - 定义泳道和任务
   - 设置网关和事件
2. 使用 deeparchi 映射到架构:
   - BPMN Pool → Business Role
   - BPMN Task → Business Process
   - BPMN Message → Application Service
```

#### 5. IT4IT + DeepArchi 协作

```
用户请求: "设计 IT 运营管理架构"

步骤:
1. 调用 it4it skill 获取价值流定义:
   - S2P (策略到组合)
   - D2F (探索到实现)
   - S2D (资源到部署)
   - C2R (消费到退役)
2. 使用 deeparchi 映射到技术层:
   - Functional Component → Application Component
   - Data Object → Data Object
   - IT Service → Technology Service
```

### 映射规则

#### ArchiMate 元素与其他框架的映射

| DeepArchi 元素 | TOGAF | DDD | BIAN | BPMN | IT4IT |
|---------------|-------|-----|------|------|-------|
| Business Role | Actor | - | Business Area | Pool | - |
| Business Process | Business Function | Domain Event Handler | Service Operation | Task | Activity |
| Business Service | Business Service | Application Service | Service Domain | - | IT Service |
| Business Object | Information Entity | Domain Event | Data Object | Data Object | - |
| Application Component | Application Component | Bounded Context | - | - | Functional Component |
| Application Service | Application Service | Domain Service | API Endpoint | Service Task | - |
| Data Object | Data Entity | Aggregate Root | Data Object | Data Object | Data Object |
| Technology Node | Platform Service | - | - | - | Infrastructure |

## 四层架构框架

DeepArchi 采用扩展的四层架构框架：

```
┌─────────────────────────────────────────────────────────────┐
│                    Business Layer (业务层)                   │
│         业务角色、业务过程、业务服务、业务对象                    │
│                      黄色系 (Yellow)                         │
├─────────────────────────────────────────────────────────────┤
│                  Application Layer (应用层)                  │
│              应用组件、应用服务、应用接口                        │
│                      绿色系 (Green)                          │
├─────────────────────────────────────────────────────────────┤
│                     Data Layer (数据层)                      │
│              数据对象、数据服务、数据库                          │
│                      蓝色系 (Blue)                           │
├─────────────────────────────────────────────────────────────┤
│                  Technology Layer (技术层)                   │
│            技术节点、系统软件、技术服务                          │
│                      绿色系 (Green)                          │
└─────────────────────────────────────────────────────────────┘
```

## 颜色规范（深浅渐变）

每层使用不同深浅的颜色区分元素类型，增强视觉层次：

### 业务层 (Business Layer) - 黄色系

| 元素类型 | 颜色代码 | 深浅 | appType |
|---------|---------|------|---------|
| Business Role (业务角色) | `#FFF8DC` | 最浅 | role |
| Business Process (业务过程) | `#FFE699` | 浅 | proc |
| Business Service (业务服务) | `#FFD54F` | 中 | serv |
| Business Object (业务对象) | `#F4B942` | 深 | passive |

### 应用层 (Application Layer) - 绿色系

| 元素类型 | 颜色代码 | 深浅 | appType |
|---------|---------|------|---------|
| Application Service (应用服务) | `#E8F5E9` | 浅 | serv |
| Application Component (应用组件) | `#66BB6A` | 深 | comp |

### 数据层 (Data Layer) - 蓝色系

| 元素类型 | 颜色代码 | 深浅 | appType |
|---------|---------|------|---------|
| Data Object (数据对象) | `#BBDEFB` | 浅 | passive |
| Data Service (数据服务) | `#64B5F6` | 中 | serv |
| Database (数据库) | `#1976D2` | 深 | comp |

### 技术层 (Technology Layer) - 绿色系

| 元素类型 | 颜色代码 | 深浅 | appType |
|---------|---------|------|---------|
| Technology Service (技术服务) | `#DCEDC8` | 浅 | serv |
| System Software (系统软件) | `#AED581` | 中 | sysSw |
| Technology Node (技术节点) | `#7CB342` | 深 | node |

## Draw.io XML 样式规范

### 核心样式结构

所有 ArchiMate 元素使用统一的形状定义：

```
shape=mxgraph.archimate3.application;appType=<类型>;archiType=<形状>;fillColor=<颜色>;strokeColor=#666666;
```

### appType 参数映射

| appType | 元素类型 | 图标 |
|---------|---------|------|
| `role` | 业务角色 | 圆柱形 |
| `proc` | 业务过程 | 箭头 |
| `serv` | 服务 | 半圆弧 |
| `passive` | 被动元素/对象 | 矩形+横线 |
| `comp` | 组件 | 组件符号 |
| `node` | 节点 | 立方体 |
| `sysSw` | 系统软件 | 齿轮 |
| `actor` | 参与者 | 小人 |

### archiType 参数

- `square` - 直角矩形（用于结构元素）
- `rounded` - 圆角矩形（用于行为元素和服务）

### 完整样式示例

```xml
<!-- 业务角色 -->
<mxCell style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=role;archiType=square;fillColor=#FFF8DC;strokeColor=#666666;" />

<!-- 业务过程 -->
<mxCell style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=proc;archiType=rounded;fillColor=#FFE699;strokeColor=#666666;" />

<!-- 业务服务 -->
<mxCell style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=serv;archiType=rounded;fillColor=#FFD54F;strokeColor=#666666;" />

<!-- 应用组件 -->
<mxCell style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=comp;archiType=square;fillColor=#66BB6A;strokeColor=#666666;" />

<!-- 数据服务 -->
<mxCell style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=serv;archiType=rounded;fillColor=#64B5F6;strokeColor=#666666;" />

<!-- 技术节点 -->
<mxCell style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=node;archiType=square;fillColor=#7CB342;strokeColor=#666666;" />
```

## 标准视图设计

### 推荐的多页面结构

创建完整的企业架构图时，建议使用以下页面结构：

| 页面 | 内容 | 用途 |
|-----|------|------|
| **Business View** | 业务角色、过程、服务、对象 | 业务能力和服务域清单 |
| **Application View** | 应用组件、应用服务 | 应用组合和服务映射 |
| **Data View** | 数据对象、数据服务、数据库 | 数据架构和信息管理 |
| **Technology View** | 技术节点、系统软件、技术服务 | 基础设施清单 |
| **Cross Layer View** | 跨层服务映射 | 垂直能力对齐 |
| **Legend** | 图例说明 | 颜色和形状参考 |

### 每页结构示例

```xml
<diagram id="business-view" name="Business View">
  <mxGraphModel>
    <root>
      <mxCell id="0" />
      <mxCell id="1" parent="0" />
      <!-- 页面说明文字 -->
      <mxCell id="note" style="text;..." value="页面描述..." />
      <!-- 架构元素 -->
      <mxCell id="element_1" style="...appType=role..." value="元素名称" />
    </root>
  </mxGraphModel>
</diagram>
```

## BIAN 框架集成

### 什么是 BIAN

BIAN (Banking Industry Architecture Network) 是银行业架构网络，提供标准化的银行业务服务域定义。

### BIAN Service Domain 示例

在 Business View 中，可以按 BIAN 服务域组织业务服务：

- **Customer Management** - 客户管理
- **Party Data Management** - 当事方数据管理
- **Product Management** - 产品管理
- **Payment Order** - 支付订单
- **Card** - 卡片服务
- **Loan** - 贷款服务
- **Risk Management** - 风险管理
- **Compliance** - 合规服务
- **Treasury** - 资金管理
- **Analytics** - 分析服务

## 最佳实践

### 1. 颜色使用原则

- **同层同色系**：同一架构层使用同一色系
- **深浅区分**：同层内用深浅区分元素类型
- **服务浅色**：服务类元素通常使用较浅颜色
- **结构深色**：核心结构元素使用较深颜色

### 2. 布局规范

- **列对齐**：同类型元素垂直对齐
- **行对齐**：相关元素水平对齐
- **间距一致**：元素间保持 60px 垂直间距
- **宽度统一**：同类元素宽度保持一致（建议 200-260px）

### 3. 命名规范

- 使用清晰、描述性的名称
- 业务层使用业务术语
- 应用层使用系统名称
- 数据层使用实体名称
- 技术层使用技术组件名称

### 4. 文档化要求

- 每页添加说明文字（页面顶部）
- 创建 Legend 页面解释颜色和图标
- 在 Cross Layer View 显示层级关系
- 添加层级标签方便识别

## 资源文件

### 模板文件

- `assets/digital-bank-archimate.drawio` - 数字银行架构示例

### 参考文档

- `references/archimate-relationships-guide.md` - 关系使用指南
- `references/drawio-archimate-tutorial.md` - Draw.io ArchiMate 教程

### 配置文件

- `assets/archimate-color-palette.json` - 颜色调色板和样式定义

### 脚本工具

- `scripts/validate-archimate.js` - ArchiMate 图表验证脚本

## 常见问题

### Q1: 元素图标不显示怎么办？

A: 确保使用正确的样式格式：
```
shape=mxgraph.archimate3.application;appType=<类型>;
```
不要使用 `shape=mxgraph.archimate3.business` 等其他格式。

### Q2: 如何区分不同类型的元素？

A: 使用深浅渐变色区分：
- 同层内从浅到深排列
- 服务类元素用浅色
- 核心结构元素用深色

### Q3: Data 层和 Application 层如何区分？

A: 
- Data 层使用蓝色系，聚焦数据对象、数据服务、数据库
- Application 层使用绿色系，聚焦应用组件和应用服务
- 将数据相关元素独立成 Data View 页面

### Q4: 如何在 Cross Layer View 展示四层关系？

A: 使用四列布局，每列代表一层：
1. 第一列：Business Layer (黄色)
2. 第二列：Application Layer (浅绿)
3. 第三列：Data Layer (蓝色)
4. 第四列：Technology Layer (深绿)

## 更新日志

- **v1.3.0** (2025-01-24):
  - 新增 archimate 技能集成 (ArchiMate 3.2 规范参考)
  - 添加 ArchiMate + DeepArchi 协作示例
  - 新增 drawio-skill 技能集成 (图表绘制工具)
  - 现已集成 8 个技能: archimate, togaf, ddd, bian, bpmn, it4it, drawio-skill

- **v1.2.0** (2025-01-24):
  - 新增集成技能支持 (togaf, ddd, bian, bpmn, it4it)
  - 添加技能协作示例和映射规则
  - 增强跨框架架构设计能力

- **v1.1.0** (2025-01-24): 
  - 新增独立的 Data Layer
  - 优化颜色方案为深浅渐变
  - 更新 Draw.io XML 样式规范
  - 添加 BIAN 框架集成指南
  - 新增 Cross Layer View 设计指南
  
- **v1.0.0** (2025-01-24): 初始版本，支持 ArchiMate 3.2 标准和 draw.io 集成

## 相关资源

- [ArchiMate 官方网站](https://www.opengroup.org/archimate)
- [Draw.io 官方网站](https://app.diagrams.net/)
- [TOGAF 官方网站](https://www.opengroup.org/togaf)
- [BIAN 银行业架构网络](https://bian.org/)
- [IT4IT 参考架构](https://www.opengroup.org/it4it)
- [DeepArchi 架构管理平台](https://www.deeparchi.com.cn)

## 关联技能

- **archimate** - ArchiMate 3.2 建模语言规范 (元素/关系/视角)
- **togaf** - TOGAF 企业架构框架
- **ddd** - 领域驱动设计
- **bian** - 银行业架构网络
- **bpmn** - 业务流程建模
- **it4it** - IT 管理参考架构
- **drawio-skill** - Draw.io 图表绘制工具
