# DeepArchi 品牌配色方案

基于 DeepArchi Logo 设计的前端和 PPT 配色方案。

## Logo 分析

Logo 特征：
- **蓝色网络球体** - 由渐变蓝色节点和连线组成，象征架构的连接性和智能化
- **深蓝色文字** - 专业、稳重、可信赖
- **红色点缀** - "i" 上的红点，增加活力和记忆点
- **中文"深度架构"** - 强调本土化和专业性

---

## 主色板

### 主色 (Primary)

| 名称 | 色值 | 预览 | 用途 |
|------|------|------|------|
| Deep Blue | `#1A3A5C` | ![#1A3A5C](https://via.placeholder.com/40/1A3A5C/1A3A5C) | 主标题、Logo文字、重要按钮 |
| Ocean Blue | `#2E6B9E` | ![#2E6B9E](https://via.placeholder.com/40/2E6B9E/2E6B9E) | 次级标题、链接、图标 |
| Sky Blue | `#4A9BD9` | ![#4A9BD9](https://via.placeholder.com/40/4A9BD9/4A9BD9) | 交互元素、进度条、高亮 |

### 辅助色 (Secondary)

| 名称 | 色值 | 预览 | 用途 |
|------|------|------|------|
| Light Cyan | `#7BC4E8` | ![#7BC4E8](https://via.placeholder.com/40/7BC4E8/7BC4E8) | 网络节点、连接线、装饰 |
| Pale Blue | `#B8E0F5` | ![#B8E0F5](https://via.placeholder.com/40/B8E0F5/B8E0F5) | 背景渐变、卡片背景 |
| Ice Blue | `#E8F4FC` | ![#E8F4FC](https://via.placeholder.com/40/E8F4FC/E8F4FC) | 页面背景、表格斑马纹 |

### 强调色 (Accent)

| 名称 | 色值 | 预览 | 用途 |
|------|------|------|------|
| Signal Red | `#E53935` | ![#E53935](https://via.placeholder.com/40/E53935/E53935) | 强调点、警告、Logo红点 |
| Coral | `#FF6B6B` | ![#FF6B6B](https://via.placeholder.com/40/FF6B6B/FF6B6B) | 次级强调、hover状态 |

### 中性色 (Neutral)

| 名称 | 色值 | 预览 | 用途 |
|------|------|------|------|
| Charcoal | `#2D3748` | ![#2D3748](https://via.placeholder.com/40/2D3748/2D3748) | 正文文字 |
| Slate | `#4A5568` | ![#4A5568](https://via.placeholder.com/40/4A5568/4A5568) | 次级文字 |
| Silver | `#A0AEC0` | ![#A0AEC0](https://via.placeholder.com/40/A0AEC0/A0AEC0) | 占位符、禁用状态 |
| Cloud | `#EDF2F7` | ![#EDF2F7](https://via.placeholder.com/40/EDF2F7/EDF2F7) | 分割线、边框 |

---

## 渐变色

### 主渐变 (Primary Gradient)
```css
background: linear-gradient(135deg, #1A3A5C 0%, #2E6B9E 50%, #4A9BD9 100%);
```
用途：Hero区域、主按钮、标题背景

### 网络渐变 (Network Gradient)
```css
background: linear-gradient(180deg, #7BC4E8 0%, #4A9BD9 50%, #2E6B9E 100%);
```
用途：模拟Logo网络球体效果

### 柔和渐变 (Subtle Gradient)
```css
background: linear-gradient(180deg, #FFFFFF 0%, #E8F4FC 100%);
```
用途：页面背景、卡片悬停

### 强调渐变 (Accent Gradient)
```css
background: linear-gradient(135deg, #E53935 0%, #FF6B6B 100%);
```
用途：CTA按钮、重要提示

---

## 前端应用

### CSS 变量

```css
:root {
  /* 主色 */
  --color-primary: #1A3A5C;
  --color-primary-light: #2E6B9E;
  --color-primary-lighter: #4A9BD9;
  
  /* 辅助色 */
  --color-secondary: #7BC4E8;
  --color-secondary-light: #B8E0F5;
  --color-background: #E8F4FC;
  
  /* 强调色 */
  --color-accent: #E53935;
  --color-accent-light: #FF6B6B;
  
  /* 文字色 */
  --color-text: #2D3748;
  --color-text-secondary: #4A5568;
  --color-text-muted: #A0AEC0;
  
  /* 边框与背景 */
  --color-border: #EDF2F7;
  --color-white: #FFFFFF;
}
```

### Tailwind CSS 配置

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        deeparchi: {
          50: '#E8F4FC',
          100: '#B8E0F5',
          200: '#7BC4E8',
          300: '#4A9BD9',
          400: '#2E6B9E',
          500: '#1A3A5C',
          600: '#153049',
          700: '#102536',
          800: '#0B1A24',
          900: '#060F12',
        },
        accent: {
          400: '#FF6B6B',
          500: '#E53935',
        }
      }
    }
  }
}
```

### 组件样式示例

#### 主按钮
```css
.btn-primary {
  background: #1A3A5C;
  color: #FFFFFF;
  border-radius: 8px;
  padding: 12px 24px;
  transition: background 0.2s;
}
.btn-primary:hover {
  background: #2E6B9E;
}
```

#### 卡片
```css
.card {
  background: #FFFFFF;
  border: 1px solid #EDF2F7;
  border-radius: 12px;
  box-shadow: 0 4px 6px -1px rgba(26, 58, 92, 0.1);
}
.card:hover {
  box-shadow: 0 10px 15px -3px rgba(26, 58, 92, 0.15);
}
```

#### 导航栏
```css
.navbar {
  background: #1A3A5C;
  color: #FFFFFF;
}
.navbar a:hover {
  background: #2E6B9E;
}
.navbar a.active {
  border-bottom: 3px solid #4A9BD9;
}
```

---

## PPT 应用

### 幻灯片背景

| 类型 | 背景 | 文字颜色 |
|------|------|----------|
| **标题页** | 渐变 `#1A3A5C → #2E6B9E` | 白色 |
| **内容页** | 纯白 `#FFFFFF` | 深灰 `#2D3748` |
| **章节页** | 渐变 `#E8F4FC → #B8E0F5` | 深蓝 `#1A3A5C` |
| **强调页** | 纯色 `#1A3A5C` | 白色 + 红点 `#E53935` |

### 文字规范

| 元素 | 颜色 | 字号 | 字重 |
|------|------|------|------|
| 主标题 | `#1A3A5C` | 44pt | Bold |
| 副标题 | `#2E6B9E` | 28pt | Semibold |
| 小标题 | `#1A3A5C` | 32pt | Bold |
| 正文 | `#2D3748` | 18pt | Normal |
| 注释 | `#4A5568` | 14pt | Normal |

### 图表配色

按优先级使用：
1. `#1A3A5C` - 主要数据
2. `#2E6B9E` - 次要数据
3. `#4A9BD9` - 第三数据
4. `#7BC4E8` - 第四数据
5. `#B8E0F5` - 第五数据
6. `#E53935` - 强调/警示数据

### 图形元素

| 元素类型 | 填充色 | 文字色 |
|----------|--------|--------|
| 主要形状 | `#1A3A5C` | 白色 |
| 次要形状 | `#4A9BD9` | 白色 |
| 辅助形状 | `#7BC4E8` | `#1A3A5C` |
| 强调形状 | `#E53935` | 白色 |
| 连接线 | `#2E6B9E` | - |
| 网络节点 | `#4A9BD9` (填充) `#1A3A5C` (描边) | - |

### 装饰元素

- **圆点图案**: 使用 `#7BC4E8` 模拟 Logo 中的网络节点
- **线条装饰**: 使用 `#E53935` 作为强调线
- **渐变圆形**: 使用网络渐变模拟 Logo 球体效果

---

## 色彩搭配示例

### 深色背景搭配
```
背景: #1A3A5C
主文字: #FFFFFF
次文字: #B8E0F5
强调: #E53935
链接: #7BC4E8
```

### 浅色背景搭配
```
背景: #FFFFFF 或 #E8F4FC
主文字: #2D3748
标题: #1A3A5C
强调: #E53935
链接: #2E6B9E
边框: #EDF2F7
```

### 卡片搭配
```
卡片背景: #FFFFFF
卡片标题: #1A3A5C
卡片内容: #4A5568
卡片图标: #4A9BD9
卡片边框: #EDF2F7
悬停阴影: rgba(26, 58, 92, 0.15)
```

---

## 无障碍对比度

| 组合 | 对比度 | WCAG 等级 |
|------|--------|-----------|
| #1A3A5C on #FFFFFF | 10.8:1 | AAA |
| #2D3748 on #FFFFFF | 9.7:1 | AAA |
| #FFFFFF on #1A3A5C | 10.8:1 | AAA |
| #E53935 on #FFFFFF | 4.6:1 | AA |
| #1A3A5C on #E8F4FC | 8.9:1 | AAA |

---

## 文件资源

- `brand-color-scheme.json` - 完整配色数据
- Logo 文件应放置在 `assets/logo/` 目录

## 相关链接

- [DeepArchi 架构管理平台](https://www.deeparchi.com.cn)
