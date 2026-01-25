#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成电影级画质的 DeepArchi 架构图
无文字，纯视觉设计
"""

from PIL import Image, ImageDraw, ImageFilter
import math
import random
import os

# 画布尺寸 (4K 画质)
WIDTH = 1920
HEIGHT = 1080

# DeepArchi 品牌色彩（电影级调色）
COLORS = {
    'primary': '#1A3A5C',
    'primary_light': '#2E6B9E',
    'primary_lighter': '#4A9BD9',
    'secondary': '#7BC4E8',
    'secondary_light': '#B8E0F5',
    'secondary_lighter': '#E8F4FC',
    'accent': '#E53935',
    'dark': '#0F1E2E',
    'white': '#FFFFFF',
}

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_gradient_background(img, draw):
    """创建电影级渐变背景"""
    # 从深蓝到浅蓝的多层渐变
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        
        # 底部深色
        r1, g1, b1 = hex_to_rgb(COLORS['dark'])
        # 中部中蓝
        r2, g2, b2 = hex_to_rgb(COLORS['primary'])
        # 顶部浅蓝
        r3, g3, b3 = hex_to_rgb(COLORS['secondary_lighter'])
        
        if ratio < 0.5:
            # 下半部分：深色到中蓝
            local_ratio = ratio * 2
            r = int(r1 + (r2 - r1) * local_ratio)
            g = int(g1 + (g2 - g1) * local_ratio)
            b = int(b1 + (b2 - b1) * local_ratio)
        else:
            # 上半部分：中蓝到浅蓝
            local_ratio = (ratio - 0.5) * 2
            r = int(r2 + (r3 - r2) * local_ratio)
            g = int(g2 + (g3 - g2) * local_ratio)
            b = int(b2 + (b3 - b2) * local_ratio)
        
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))

def draw_glowing_node(draw, x, y, size, color, glow_intensity=0.3):
    """绘制发光节点"""
    # 外发光层
    for i in range(3):
        alpha = int(255 * glow_intensity * (1 - i/3))
        glow_size = size + (i + 1) * 8
        glow_color = (*hex_to_rgb(color), alpha)
        # 使用椭圆绘制发光效果
        draw.ellipse([x-glow_size, y-glow_size, x+glow_size, y+glow_size], 
                    fill=glow_color)
    
    # 核心节点
    draw.ellipse([x-size, y-size, x+size, y+size], fill=hex_to_rgb(color))

def draw_network_connection(draw, x1, y1, x2, y2, color, width=2, opacity=0.4):
    """绘制网络连接线（带渐变）"""
    # 计算距离
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    steps = int(dist / 2)
    
    if steps < 1:
        return
    
    # 绘制渐变连线
    for i in range(steps):
        ratio = i / steps
        x = int(x1 + (x2 - x1) * ratio)
        y = int(y1 + (y2 - y1) * ratio)
        
        # 中间亮，两端暗
        intensity = 1 - abs(ratio - 0.5) * 2
        alpha = int(255 * opacity * intensity)
        line_color = (*hex_to_rgb(color), alpha)
        
        draw.ellipse([x-width, y-width, x+width, y+width], fill=line_color)

def draw_architecture_layer_visual(draw, center_x, center_y, radius, color, layer_index):
    """绘制架构层级的视觉表现（无文字）"""
    # 主圆形
    draw.ellipse([center_x-radius, center_y-radius, center_x+radius, center_y+radius],
                fill=hex_to_rgb(color), outline=None)
    
    # 内圈高光
    inner_radius = radius * 0.7
    highlight_color = tuple(min(255, c + 40) for c in hex_to_rgb(color))
    draw.ellipse([center_x-inner_radius, center_y-inner_radius, 
                 center_x+inner_radius, center_y+inner_radius],
                fill=highlight_color)
    
    # 外圈发光
    glow_radius = radius * 1.3
    glow_alpha = 60
    glow_color = (*hex_to_rgb(color), glow_alpha)
    draw.ellipse([center_x-glow_radius, center_y-glow_radius,
                 center_x+glow_radius, center_y+glow_radius],
                fill=glow_color)
    
    # 内部装饰节点
    num_nodes = 8 + layer_index * 2
    for i in range(num_nodes):
        angle = (i / num_nodes) * 2 * math.pi
        node_dist = inner_radius * 0.6
        node_x = center_x + node_dist * math.cos(angle)
        node_y = center_y + node_dist * math.sin(angle)
        draw_glowing_node(draw, int(node_x), int(node_y), 4, COLORS['white'], 0.2)

def create_cinematic_diagram():
    """创建电影级架构图"""
    # 创建画布
    img = Image.new('RGB', (WIDTH, HEIGHT), hex_to_rgb(COLORS['dark']))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # 背景渐变
    create_gradient_background(img, draw)
    
    # 设置随机种子以保证可重复性
    random.seed(42)
    
    # 创建网络节点系统
    num_main_nodes = 25
    main_nodes = []
    
    # 生成主要节点位置（形成层次结构）
    for i in range(num_main_nodes):
        if i < 4:
            # 前4个作为主要架构层节点
            angle = (i / 4) * 2 * math.pi - math.pi/2
            radius = 200
            x = WIDTH // 2 + radius * math.cos(angle)
            y = HEIGHT // 2 + radius * math.sin(angle)
            size = 25
            layer_colors = ['#F4B942', '#66BB6A', '#4A9BD9', '#7CB342']
            color = layer_colors[i]
        else:
            # 其他节点随机分布
            x = random.uniform(WIDTH * 0.1, WIDTH * 0.9)
            y = random.uniform(HEIGHT * 0.1, HEIGHT * 0.9)
            size = random.uniform(8, 15)
            color = COLORS['primary_lighter']
        
        main_nodes.append((x, y, size, color))
    
    # 绘制连接线（先绘制，在节点下方）
    for i, (x1, y1, s1, c1) in enumerate(main_nodes):
        for j, (x2, y2, s2, c2) in enumerate(main_nodes[i+1:], i+1):
            dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            if dist < 300:  # 只连接相近的节点
                # 使用主色调或节点颜色
                line_color = COLORS['primary_lighter']
                draw_network_connection(draw, int(x1), int(y1), int(x2), int(y2), 
                                      line_color, width=1, opacity=0.15)
    
    # 绘制主要架构层节点（4个）
    layer_colors = ['#F4B942', '#66BB6A', '#4A9BD9', '#7CB342']
    for i in range(4):
        angle = (i / 4) * 2 * math.pi - math.pi/2
        radius = 200
        x = WIDTH // 2 + radius * math.cos(angle)
        y = HEIGHT // 2 + radius * math.sin(angle)
        draw_architecture_layer_visual(draw, int(x), int(y), 60, layer_colors[i], i)
    
    # 绘制其他节点
    for x, y, size, color in main_nodes[4:]:
        draw_glowing_node(draw, int(x), int(y), int(size), color, 0.25)
    
    # 添加装饰性粒子效果
    for _ in range(100):
        x = random.uniform(0, WIDTH)
        y = random.uniform(0, HEIGHT)
        size = random.uniform(1, 3)
        alpha = random.uniform(20, 80)
        particle_color = (*hex_to_rgb(COLORS['primary_lighter']), int(alpha))
        draw.ellipse([x-size, y-size, x+size, y+size], fill=particle_color)
    
    # 添加光晕效果（中心区域）
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    for i in range(5):
        glow_radius = 150 + i * 50
        alpha = 30 - i * 5
        glow_color = (*hex_to_rgb(COLORS['secondary']), alpha)
        draw.ellipse([center_x-glow_radius, center_y-glow_radius,
                     center_x+glow_radius, center_y+glow_radius],
                    fill=glow_color)
    
    # 添加顶部和底部的深度渐变遮罩
    overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    
    # 顶部渐变遮罩
    for y in range(HEIGHT // 4):
        alpha = int(40 * (1 - y / (HEIGHT // 4)))
        overlay_draw.line([(0, y), (WIDTH, y)], fill=(0, 0, 0, alpha))
    
    # 底部渐变遮罩
    for y in range(HEIGHT - HEIGHT // 4, HEIGHT):
        local_y = y - (HEIGHT - HEIGHT // 4)
        alpha = int(40 * (local_y / (HEIGHT // 4)))
        overlay_draw.line([(0, y), (WIDTH, y)], fill=(0, 0, 0, alpha))
    
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    
    return img

if __name__ == "__main__":
    print("正在生成电影级架构图...")
    img = create_cinematic_diagram()
    
    # 保存为高质量 JPEG
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "architecture-diagram.jpg")
    img.save(output_path, "JPEG", quality=98, optimize=False)
    print(f"架构图已保存至: {output_path}")
    
    # 同时保存为 PNG（无损）
    png_path = os.path.join(script_dir, "architecture-diagram.png")
    img.save(png_path, "PNG", optimize=False)
    print(f"PNG 版本已保存至: {png_path}")
