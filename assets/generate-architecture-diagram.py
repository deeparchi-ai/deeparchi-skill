#!/usr/bin/env python3
"""
生成 DeepArchi 企业架构图高清图片
基于 "Network Precision" 设计哲学
"""

from PIL import Image, ImageDraw, ImageFont
import math
import random

# 固定随机种子，保证装饰性网络节点每次生成结果可复现
random.seed(42)

# 画布尺寸 (高清)
WIDTH = 1200
HEIGHT = 800

# DeepArchi 品牌色彩
COLORS = {
    'primary': '#1A3A5C',
    'primary_light': '#2E6B9E',
    'primary_lighter': '#4A9BD9',
    'secondary': '#7BC4E8',
    'secondary_light': '#B8E0F5',
    'secondary_lighter': '#E8F4FC',
    'accent': '#E53935',
    'white': '#FFFFFF',
    'text': '#2D3748',
    'text_secondary': '#4A5568',
}

def hex_to_rgb(hex_color):
    """转换十六进制颜色为RGB元组"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def draw_network_sphere(draw, center_x, center_y, radius, opacity=0.3):
    """绘制网络球体装饰"""
    # 创建渐变网络节点
    num_nodes = 40
    nodes = []
    
    for i in range(num_nodes):
        angle = (i / num_nodes) * 2 * math.pi
        distance = random.uniform(radius * 0.3, radius * 0.9)
        x = center_x + distance * math.cos(angle)
        y = center_y + distance * math.sin(angle)
        size = random.uniform(3, 6)
        nodes.append((x, y, size))
    
    # 绘制连接线
    for i, (x1, y1, s1) in enumerate(nodes):
        for j, (x2, y2, s2) in enumerate(nodes[i+1:], i+1):
            dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            if dist < radius * 0.5:
                # 渐变蓝色连线
                alpha = int(255 * opacity * (1 - dist / (radius * 0.5)))
                color = (*hex_to_rgb(COLORS['primary_lighter']), alpha)
                draw.line([(x1, y1), (x2, y2)], fill=color, width=1)
    
    # 绘制节点
    for x, y, size in nodes:
        # 从中心到边缘的渐变
        dist_from_center = math.sqrt((x-center_x)**2 + (y-center_y)**2)
        intensity = 1 - (dist_from_center / radius)
        
        if intensity > 0.5:
            color = hex_to_rgb(COLORS['primary'])
        elif intensity > 0.3:
            color = hex_to_rgb(COLORS['primary_light'])
        else:
            color = hex_to_rgb(COLORS['secondary'])
        
        draw.ellipse([x-size, y-size, x+size, y+size], fill=color)

def draw_architecture_layer(draw, x, y, width, height, layer_name, layer_desc, layer_color, icon_emoji):
    """绘制架构层级卡片"""
    # 卡片背景
    draw.rounded_rectangle(
        [x, y, x+width, y+height],
        radius=12,
        fill=hex_to_rgb(COLORS['white']),
        outline=hex_to_rgb(COLORS['secondary_lighter']),
        width=1
    )
    
    # 左侧彩色边框
    border_width = 4
    draw.rectangle(
        [x, y, x+border_width, y+height],
        fill=hex_to_rgb(layer_color)
    )
    
    # 图标区域
    icon_size = 48
    icon_x = x + 24
    icon_y = y + 24
    
    # 图标背景（圆形）
    icon_bg_size = icon_size + 8
    draw.ellipse(
        [icon_x - icon_bg_size//2, icon_y - icon_bg_size//2,
         icon_x + icon_bg_size//2, icon_y + icon_bg_size//2],
        fill=hex_to_rgb(layer_color)
    )
    
    # 文字区域
    text_x = x + 90
    text_y = y + 24
    
    # 层级名称
    try:
        font_large = ImageFont.truetype("arial.ttf", 18)
        font_small = ImageFont.truetype("arial.ttf", 13)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    draw.text((text_x, text_y), layer_name, fill=hex_to_rgb(COLORS['text']), font=font_large)
    draw.text((text_x, text_y + 26), layer_desc, fill=hex_to_rgb(COLORS['text_secondary']), font=font_small)

def create_architecture_diagram():
    """创建架构图主函数"""
    # 创建画布
    img = Image.new('RGB', (WIDTH, HEIGHT), hex_to_rgb(COLORS['white']))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # 背景渐变
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r1, g1, b1 = hex_to_rgb(COLORS['white'])
        r2, g2, b2 = hex_to_rgb(COLORS['secondary_lighter'])
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))
    
    # 绘制装饰性网络球体（右上角，半透明）
    draw_network_sphere(draw, WIDTH - 150, 100, 200, opacity=0.15)
    
    # 主容器区域
    container_x = 100
    container_y = 80
    container_width = WIDTH - 200
    container_height = HEIGHT - 160
    
    # 主容器背景（带阴影效果）
    shadow_offset = 8
    draw.rounded_rectangle(
        [container_x + shadow_offset, container_y + shadow_offset,
         container_x + container_width + shadow_offset, container_y + container_height + shadow_offset],
        radius=20,
        fill=hex_to_rgb(COLORS['secondary_lighter'])
    )
    
    draw.rounded_rectangle(
        [container_x, container_y, container_x + container_width, container_y + container_height],
        radius=20,
        fill=hex_to_rgb(COLORS['white']),
        outline=hex_to_rgb(COLORS['secondary_lighter']),
        width=2
    )
    
    # 标题
    try:
        font_title = ImageFont.truetype("arial.ttf", 36)
        font_badge = ImageFont.truetype("arial.ttf", 12)
    except:
        font_title = ImageFont.load_default()
        font_badge = ImageFont.load_default()
    
    title_x = container_x + container_width // 2
    title_y = container_y + 50
    
    # 标题文字
    title_text = "Architecture Diagram"
    bbox = draw.textbbox((0, 0), title_text, font=font_title)
    text_width = bbox[2] - bbox[0]
    draw.text((title_x - text_width // 2, title_y), title_text, 
              fill=hex_to_rgb(COLORS['primary']), font=font_title)
    
    # 徽章
    badge_x = container_x + container_width - 120
    badge_y = container_y + 30
    draw.rounded_rectangle(
        [badge_x, badge_y, badge_x + 100, badge_y + 24],
        radius=12,
        fill=hex_to_rgb(COLORS['white']),
        outline=hex_to_rgb(COLORS['secondary_lighter']),
        width=1
    )
    draw.text((badge_x + 10, badge_y + 6), "ArchiMate 3.2", 
              fill=hex_to_rgb(COLORS['primary']), font=font_badge)
    
    # 绘制四层架构
    layer_width = container_width - 80
    layer_height = 70
    layer_spacing = 20
    start_y = title_y + 80
    
    layers = [
        ("Business Layer", "业务角色、流程、服务、对象", "#F4B942", "💼"),
        ("Application Layer", "应用组件、服务、接口", "#66BB6A", "📱"),
        ("Data Layer", "数据对象、服务、数据库", "#4A9BD9", "🗄️"),
        ("Technology Layer", "节点、系统软件、基础设施", "#7CB342", "⚙️"),
    ]
    
    for i, (name, desc, color, icon) in enumerate(layers):
        y_pos = start_y + i * (layer_height + layer_spacing)
        draw_architecture_layer(
            draw,
            container_x + 40,
            y_pos,
            layer_width,
            layer_height,
            name,
            desc,
            color,
            icon
        )
    
    # 底部统计信息
    stats_y = start_y + 4 * (layer_height + layer_spacing) + 30
    stats = [
        ("100+", "架构元素"),
        ("25+", "标准视角"),
        ("7", "架构层次"),
    ]
    
    stat_width = (layer_width - 40) // 3
    for i, (value, label) in enumerate(stats):
        stat_x = container_x + 40 + i * stat_width
        stat_center_x = stat_x + stat_width // 2
        
        # 数值
        try:
            font_stat = ImageFont.truetype("arial.ttf", 24)
            font_label = ImageFont.truetype("arial.ttf", 12)
        except:
            font_stat = ImageFont.load_default()
            font_label = ImageFont.load_default()
        
        bbox = draw.textbbox((0, 0), value, font=font_stat)
        text_width = bbox[2] - bbox[0]
        draw.text((stat_center_x - text_width // 2, stats_y), value,
                  fill=hex_to_rgb(COLORS['primary']), font=font_stat)
        
        # 标签
        bbox = draw.textbbox((0, 0), label, font=font_label)
        text_width = bbox[2] - bbox[0]
        draw.text((stat_center_x - text_width // 2, stats_y + 32), label,
                  fill=hex_to_rgb(COLORS['text_secondary']), font=font_label)
    
    # 装饰性网络节点（左下角）
    draw_network_sphere(draw, 200, HEIGHT - 150, 150, opacity=0.1)
    
    return img

if __name__ == "__main__":
    import os
    print("正在生成架构图...")
    img = create_architecture_diagram()
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "architecture-diagram.jpg")
    img.save(output_path, "JPEG", quality=95, optimize=True)
    print(f"架构图已保存至: {output_path}")
