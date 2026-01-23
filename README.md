# DeepArchi Skill - ArchiMate 架构建模

## 概述

DeepArchi Skill 是一个专门用于创建符合 ArchiMate 3.2 标准的企业架构图的技能。该技能集成了 draw.io 工具，帮助架构师快速创建标准化的企业架构视图。

## 何时使用

当用户需要：
- 创建符合 ArchiMate 标准的企业架构图
- 使用 draw.io 绘制架构视图
- 生成业务架构、应用架构、技术架构等视图
- 创建架构资产的可视化表达
- 遵循 TOGAF 和 ArchiMate 标准的架构设计

## ArchiMate 3.2 核心概念

### 三层架构框架

ArchiMate 定义了三个主要层次：

1. **业务层（Business Layer）**
   - 业务角色、业务服务、业务流程
   - 业务对象、业务事件

2. **应用层（Application Layer）**
   - 应用组件、应用服务
   - 应用接口、数据对象

3. **技术层（Technology Layer）**
   - 技术节点、技术服务
   - 设备、系统软件、网络

### 核心元素类型

#### 结构元素（Structure Elements）
- **业务层**：业务角色、业务协作、业务接口、业务对象
- **应用层**：应用组件、应用协作、应用接口、数据对象
- **技术层**：节点、设备、系统软件、网络、通信路径

#### 行为元素（Behavior Elements）
- **业务层**：业务流程、业务功能、业务交互、业务事件
- **应用层**：应用功能、应用交互、应用流程
- **技术层**：技术服务、技术功能、技术交互、技术流程

#### 被动结构元素（Passive Structure Elements）
- **业务层**：业务对象、合约
- **应用层**：数据对象
- **技术层**：工件

### 关系类型

- **组合关系（Composition）**：实线，带实心菱形
- **聚合关系（Aggregation）**：实线，带空心菱形
- **分配关系（Assignment）**：实线箭头
- **实现关系（Realization）**：虚线箭头
- **服务关系（Serving）**：实线箭头
- **访问关系（Access）**：虚线箭头
- **关联关系（Association）**：实线箭头
- **触发关系（Triggering）**：虚线箭头
- **影响关系（Influence）**：虚线箭头
- **特殊化关系（Specialization）**：实线箭头
- **流关系（Flow）**：实线箭头

## Draw.io 使用指南

### 1. 创建 ArchiMate 图表

在 draw.io 中创建 ArchiMate 图表：

1. 打开 draw.io (https://app.diagrams.net/)
2. 选择 "Create New Diagram"
3. 选择 "Blank Diagram" 或使用 ArchiMate 模板

### 2. 使用 ArchiMate 形状库

draw.io 支持 ArchiMate 形状库：

1. 在左侧面板点击 "More Shapes"
2. 搜索 "ArchiMate" 或 "ArchiMate 3.2"
3. 启用 ArchiMate 形状库
4. 现在可以使用所有 ArchiMate 元素

### 3. 创建标准视图

#### 业务架构视图
- 使用业务层元素：业务角色、业务流程、业务服务
- 展示业务能力、价值链、业务流程

#### 应用架构视图
- 使用应用层元素：应用组件、应用服务、应用接口
- 展示应用系统、服务架构、数据流

#### 技术架构视图
- 使用技术层元素：节点、设备、系统软件、网络
- 展示基础设施、部署架构、技术栈

#### 跨层视图
- 结合业务、应用、技术三层元素
- 展示端到端的架构关系

### 4. 颜色规范

ArchiMate 标准颜色方案：

- **业务层**：黄色系（#FFF2CC, #FFD966）
- **应用层**：蓝色系（#D5E8D4, #97D077）
- **技术层**：绿色系（#D5E8D4, #97D077）
- **动机层**：紫色系（#E1D5E7, #9673A6）
- **实施与迁移层**：灰色系（#F5F5F5, #D0D0D0）

### 5. 命名规范

- 使用清晰、描述性的名称
- 遵循驼峰命名或下划线命名
- 包含版本号（如：v1.0）
- 使用中文或英文，保持一致性

## 最佳实践

### 1. 视图设计原则

- **单一关注点**：每个视图聚焦一个特定方面
- **层次清晰**：明确展示架构层次关系
- **关系明确**：正确使用关系类型
- **标注完整**：添加必要的说明和标注

### 2. 元素使用规范

- 使用标准 ArchiMate 元素，避免自定义形状
- 保持元素大小和比例一致
- 对齐和间距要规范
- 使用连接器而非自由线条

### 3. 文档化要求

- 为每个视图添加标题和说明
- 包含图例说明元素和关系含义
- 标注创建日期和版本信息
- 添加作者和审核信息

## 示例场景

### 场景 1：创建业务架构视图

```
1. 创建新的 draw.io 图表
2. 添加业务角色（如：客户、银行、监管机构）
3. 添加业务流程（如：开户流程、支付流程）
4. 使用服务关系连接业务角色和业务流程
5. 添加业务服务（如：账户管理服务、支付服务）
6. 使用实现关系连接业务流程和业务服务
```

### 场景 2：创建应用架构视图

```
1. 创建新的 draw.io 图表
2. 添加应用组件（如：核心系统、支付系统、风控系统）
3. 添加应用接口（如：REST API、消息队列接口）
4. 使用服务关系连接应用组件
5. 添加数据对象（如：账户数据、交易数据）
6. 使用访问关系连接应用组件和数据对象
```

### 场景 3：创建技术架构视图

```
1. 创建新的 draw.io 图表
2. 添加技术节点（如：应用服务器、数据库服务器）
3. 添加系统软件（如：操作系统、中间件、数据库）
4. 添加网络和通信路径
5. 使用分配关系连接系统软件和技术节点
6. 使用通信路径连接不同节点
```

## 资源文件

### 模板文件

- `templates/business-architecture-template.drawio` - 业务架构模板
- `templates/application-architecture-template.drawio` - 应用架构模板
- `templates/technology-architecture-template.drawio` - 技术架构模板
- `templates/cross-layer-template.drawio` - 跨层架构模板

### 参考文档

- `references/archimate-3.2-specification.pdf` - ArchiMate 3.2 规范
- `references/archimate-relationships-guide.md` - 关系使用指南
- `references/drawio-archimate-tutorial.md` - Draw.io ArchiMate 教程

### 脚本工具

- `scripts/validate-archimate.js` - ArchiMate 图表验证脚本
- `scripts/export-to-archi.js` - 导出到 Archi 工具脚本

## 与 DeepArchi 平台集成

### 架构资产管理

创建的 ArchiMate 图表可以：
1. 导入到 DeepArchi 架构管理平台
2. 与架构元模型绑定
3. 生成架构资产视图
4. 支持架构资产保鲜

### 架构设计流程

1. **设计阶段**：使用本技能创建架构图
2. **评审阶段**：在 DeepArchi 平台进行在线评审
3. **管理阶段**：作为架构资产纳入管理
4. **演进阶段**：跟踪架构变更历史

## 常见问题

### Q1: 如何在 draw.io 中找不到 ArchiMate 形状？

A: 确保在 "More Shapes" 中启用了 ArchiMate 3.2 形状库。如果仍然找不到，可以手动导入 ArchiMate 形状库文件。

### Q2: 如何确保图表符合 ArchiMate 标准？

A: 使用本技能提供的验证脚本检查图表，确保：
- 只使用标准 ArchiMate 元素
- 关系类型使用正确
- 层次结构符合规范

### Q3: 如何导出图表到其他工具？

A: 可以导出为：
- PNG/SVG 图片格式
- XML 格式（draw.io 原生格式）
- 使用脚本转换为 Archi 工具格式

## 更新日志

- **v1.0.0** (2025-01-24): 初始版本，支持 ArchiMate 3.2 标准和 draw.io 集成

## 相关资源

- [ArchiMate 官方网站](https://www.opengroup.org/archimate)
- [Draw.io 官方网站](https://app.diagrams.net/)
- [DeepArchi 架构管理平台](https://deeparchi.com)
