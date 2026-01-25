# DeepArchi Skill 使用示例

## 示例 1：创建数字银行四层架构视图

### 场景描述
为数字银行创建完整的四层架构视图，包含 Business、Application、Data、Technology 层，以及 Cross Layer View 和 Legend。

### Draw.io 文件结构

```xml
<mxfile pages="6">
  <diagram id="business-view" name="Business View">...</diagram>
  <diagram id="application-view" name="Application View">...</diagram>
  <diagram id="data-view" name="Data View">...</diagram>
  <diagram id="technology-view" name="Technology View">...</diagram>
  <diagram id="cross-layer" name="Cross Layer View">...</diagram>
  <diagram id="legend" name="Legend">...</diagram>
</mxfile>
```

### Business View 示例

```xml
<!-- 页面说明 -->
<mxCell id="b_note" style="text;html=1;strokeColor=none;fillColor=none;" 
        value="BIAN Business View: 业务服务域清单" />

<!-- 业务角色 - 最浅黄 #FFF8DC -->
<mxCell id="b_role_1" 
        style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=role;archiType=square;fillColor=#FFF8DC;strokeColor=#666666;" 
        value="Customer" />

<!-- 业务过程 - 浅黄 #FFE699 -->
<mxCell id="b_proc_1" 
        style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=proc;archiType=rounded;fillColor=#FFE699;strokeColor=#666666;" 
        value="Customer Onboarding" />

<!-- 业务服务 - 中黄 #FFD54F -->
<mxCell id="b_srv_1" 
        style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=serv;archiType=rounded;fillColor=#FFD54F;strokeColor=#666666;" 
        value="Customer Management (BIAN)" />

<!-- 业务对象 - 深黄 #F4B942 -->
<mxCell id="b_obj_1" 
        style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=passive;archiType=square;fillColor=#F4B942;strokeColor=#666666;" 
        value="Customer Profile" />
```

### Application View 示例

```xml
<!-- 应用组件 - 深绿 #66BB6A -->
<mxCell id="a_comp_1" 
        style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=comp;archiType=square;fillColor=#66BB6A;strokeColor=#666666;" 
        value="Customer Management System" />

<!-- 应用服务 - 浅绿 #E8F5E9 -->
<mxCell id="a_srv_1" 
        style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=serv;archiType=rounded;fillColor=#E8F5E9;strokeColor=#666666;" 
        value="Customer Management Service" />
```

### Data View 示例

```xml
<!-- 数据对象 - 浅蓝 #BBDEFB -->
<mxCell id="d_obj_1" 
        style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=passive;archiType=square;fillColor=#BBDEFB;strokeColor=#666666;" 
        value="Customer Data" />

<!-- 数据服务 - 中蓝 #64B5F6 -->
<mxCell id="d_srv_1" 
        style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=serv;archiType=rounded;fillColor=#64B5F6;strokeColor=#666666;" 
        value="Customer Data Service" />

<!-- 数据库 - 深蓝 #1976D2 (白字) -->
<mxCell id="d_db_1" 
        style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=comp;archiType=square;fillColor=#1976D2;strokeColor=#666666;fontColor=#FFFFFF;" 
        value="Customer DB" />
```

### Technology View 示例

```xml
<!-- 技术节点 - 深绿 #7CB342 -->
<mxCell id="t_node_1" 
        style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=node;archiType=square;fillColor=#7CB342;strokeColor=#666666;" 
        value="API Gateway Cluster" />

<!-- 系统软件 - 中绿 #AED581 -->
<mxCell id="t_sys_1" 
        style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=sysSw;archiType=square;fillColor=#AED581;strokeColor=#666666;" 
        value="Kubernetes" />

<!-- 技术服务 - 浅绿 #DCEDC8 -->
<mxCell id="t_srv_1" 
        style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=serv;archiType=rounded;fillColor=#DCEDC8;strokeColor=#666666;" 
        value="API Management" />
```

## 示例 2：Cross Layer View 四列布局

### 场景描述
创建跨层视图，展示四层架构的垂直对齐关系。

### 布局结构

```
┌──────────────┬──────────────┬──────────────┬──────────────┐
│ Business     │ Application  │ Data         │ Technology   │
│ Layer        │ Layer        │ Layer        │ Layer        │
├──────────────┼──────────────┼──────────────┼──────────────┤
│ Customer     │ Customer     │ Customer     │ API          │
│ Management   │ Mgmt Service │ Data Service │ Management   │
│ (BIAN)       │              │              │              │
├──────────────┼──────────────┼──────────────┼──────────────┤
│ Payment      │ Payment      │ Transaction  │ Data         │
│ Order (BIAN) │ Service      │ Data Service │ Storage      │
├──────────────┼──────────────┼──────────────┼──────────────┤
│ ...          │ ...          │ ...          │ ...          │
└──────────────┴──────────────┴──────────────┴──────────────┘
     #FFD54F       #E8F5E9        #64B5F6        #DCEDC8
```

### XML 示例

```xml
<diagram id="cross-layer" name="Cross Layer View">
  <mxGraphModel>
    <root>
      <mxCell id="0" />
      <mxCell id="1" parent="0" />
      
      <!-- 说明文字 -->
      <mxCell id="c_note" style="text;html=1;" 
              value="Cross Layer View: 四层架构垂直对齐" />
      
      <!-- 第一列: Business (x=40) -->
      <mxCell id="c_bsrv_1" 
              style="...;fillColor=#FFD54F;..." 
              value="Customer Management (BIAN)">
        <mxGeometry x="40" y="60" width="220" height="50" />
      </mxCell>
      
      <!-- 第二列: Application (x=300) -->
      <mxCell id="c_asrv_1" 
              style="...;fillColor=#E8F5E9;..." 
              value="Customer Mgmt Service">
        <mxGeometry x="300" y="60" width="220" height="50" />
      </mxCell>
      
      <!-- 第三列: Data (x=560) -->
      <mxCell id="c_dsrv_1" 
              style="...;fillColor=#64B5F6;..." 
              value="Customer Data Service">
        <mxGeometry x="560" y="60" width="220" height="50" />
      </mxCell>
      
      <!-- 第四列: Technology (x=820) -->
      <mxCell id="c_tsrv_1" 
              style="...;fillColor=#DCEDC8;..." 
              value="API Management">
        <mxGeometry x="820" y="60" width="220" height="50" />
      </mxCell>
      
      <!-- 底部标签 -->
      <mxCell id="c_label_b" style="text;fontColor=#B8860B;fontStyle=1;" 
              value="Business Layer">
        <mxGeometry x="40" y="300" width="220" height="20" />
      </mxCell>
      <!-- ... 其他标签 ... -->
    </root>
  </mxGraphModel>
</diagram>
```

## 示例 3：Legend 页面设计

### 场景描述
创建图例页面，解释所有颜色和形状的含义。

### 布局结构

```
┌────────────────────────────────────────────────────────────────────┐
│ Legend: 颜色和形状参考 (ArchiMate 3.2)                               │
├─────────────────┬────────────────┬────────────────┬────────────────┤
│ Business Layer  │ Application    │ Data Layer     │ Technology     │
│ (业务层)        │ Layer (应用层) │ (数据层)       │ Layer (技术层) │
├─────────────────┼────────────────┼────────────────┼────────────────┤
│ [Role]          │ [Component]    │ [Data Object]  │ [Node]         │
│ #FFF8DC         │ #66BB6A        │ #BBDEFB        │ #7CB342        │
├─────────────────┼────────────────┼────────────────┼────────────────┤
│ [Process]       │ [Service]      │ [Data Service] │ [System SW]    │
│ #FFE699         │ #E8F5E9        │ #64B5F6        │ #AED581        │
├─────────────────┼────────────────┼────────────────┼────────────────┤
│ [Service]       │                │ [Database]     │ [Service]      │
│ #FFD54F         │                │ #1976D2        │ #DCEDC8        │
├─────────────────┤                ├────────────────┤                │
│ [Object]        │                │                │                │
│ #F4B942         │                │                │                │
└─────────────────┴────────────────┴────────────────┴────────────────┘
```

## 示例 4：BIAN 服务域映射

### 场景描述
按照 BIAN (Banking Industry Architecture Network) 框架组织业务服务域。

### BIAN 核心服务域

| BIAN Service Domain | 中文名称 | 业务能力 |
|---------------------|---------|---------|
| Customer Management | 客户管理 | 客户生命周期管理 |
| Party Data Management | 当事方数据管理 | KYC/AML |
| Product Management | 产品管理 | 产品目录和定价 |
| Payment Order | 支付订单 | 支付执行 |
| Card | 卡片服务 | 发卡和卡交易 |
| Loan | 贷款服务 | 贷款发放和管理 |
| Risk Management | 风险管理 | 风险评估和控制 |
| Compliance | 合规服务 | 监管报告 |
| Treasury | 资金管理 | 流动性管理 |
| Analytics | 分析服务 | 数据分析和报告 |

### XML 示例

```xml
<!-- BIAN Customer Management -->
<mxCell id="bian_cm" 
        style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=serv;archiType=rounded;fillColor=#FFD54F;strokeColor=#666666;" 
        value="Customer Management (BIAN)">
  <mxGeometry x="500" y="60" width="260" height="50" />
</mxCell>

<!-- BIAN Payment Order -->
<mxCell id="bian_po" 
        style="html=1;outlineConnect=0;whiteSpace=wrap;shape=mxgraph.archimate3.application;appType=serv;archiType=rounded;fillColor=#FFD54F;strokeColor=#666666;" 
        value="Payment Order (BIAN)">
  <mxGeometry x="500" y="120" width="260" height="50" />
</mxCell>
```

## 示例 5：元素几何布局规范

### 标准尺寸

| 元素类型 | 宽度 | 高度 | 说明 |
|---------|-----|------|------|
| 标准元素 | 200-260 | 50 | 适合单行文字 |
| 宽元素 | 300-400 | 50 | 适合长名称 |
| 方形元素 | 160 | 50 | 简短名称 |

### 间距规范

| 间距类型 | 数值 | 说明 |
|---------|-----|------|
| 垂直间距 | 60px | 元素行间距 |
| 水平间距 | 40px | 元素列间距 |
| 列宽 | 240-280px | 每列元素区域 |
| 页面边距 | 40px | 距页面边缘 |

### 坐标示例

```xml
<!-- 第一列 (x=40) -->
<mxGeometry x="40" y="60" width="160" height="50" />   <!-- Row 1 -->
<mxGeometry x="40" y="120" width="160" height="50" />  <!-- Row 2 -->
<mxGeometry x="40" y="180" width="160" height="50" />  <!-- Row 3 -->

<!-- 第二列 (x=240) -->
<mxGeometry x="240" y="60" width="220" height="50" />  <!-- Row 1 -->
<mxGeometry x="240" y="120" width="220" height="50" /> <!-- Row 2 -->

<!-- 第三列 (x=500) -->
<mxGeometry x="500" y="60" width="260" height="50" />  <!-- Row 1 -->
```

## 最佳实践提示

### 1. 颜色一致性
- 始终使用定义好的颜色代码
- 同层元素使用同色系
- 用深浅区分元素类型

### 2. 样式标准化
- 统一使用 `shape=mxgraph.archimate3.application`
- 正确设置 `appType` 参数
- 服务用 `archiType=rounded`，结构用 `archiType=square`

### 3. 布局规范
- 保持元素对齐
- 使用一致的间距
- 每页添加说明文字

### 4. 命名规范
- 业务层使用业务术语
- 应用层使用系统名称
- 数据层使用实体名称
- 技术层使用技术组件名称

### 5. 文档化
- 每页顶部添加说明
- 创建 Legend 页面
- 在 Cross Layer View 展示层级关系

## 参考文件

完整示例请参考：
- `assets/digital-bank-archimate.drawio` - 数字银行四层架构完整示例
- `assets/archimate-color-palette.json` - 颜色和样式定义
