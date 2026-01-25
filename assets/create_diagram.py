# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import math, random, os

WIDTH, HEIGHT = 1200, 800
COLORS = {
    'primary': '#1A3A5C',
    'primary_light': '#2E6B9E', 
    'primary_lighter': '#4A9BD9',
    'secondary': '#7BC4E8',
    'secondary_lighter': '#E8F4FC',
    'white': '#FFFFFF',
    'text': '#2D3748',
    'text_secondary': '#4A5568'
}

def hex_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

img = Image.new('RGB', (WIDTH, HEIGHT), hex_rgb(COLORS['white']))
draw = ImageDraw.Draw(img, 'RGBA')

# 背景渐变
for y in range(HEIGHT):
    r = int(255 + (232-255) * y/HEIGHT)
    g = int(255 + (244-255) * y/HEIGHT)
    b = int(255 + (252-255) * y/HEIGHT)
    draw.line([(0,y), (WIDTH,y)], fill=(r,g,b))

# 主容器
cx, cy, cw, ch = 100, 80, 1000, 640
draw.rounded_rectangle([cx+8, cy+8, cx+cw+8, cy+ch+8], radius=20, fill=hex_rgb(COLORS['secondary_lighter']))
draw.rounded_rectangle([cx, cy, cx+cw, cy+ch], radius=20, fill=hex_rgb(COLORS['white']), outline=hex_rgb(COLORS['secondary_lighter']), width=2)

# 标题
try:
    ft = ImageFont.truetype('arial.ttf', 36)
    fb = ImageFont.truetype('arial.ttf', 12)
    fl = ImageFont.truetype('arial.ttf', 18)
    fs = ImageFont.truetype('arial.ttf', 13)
    fst = ImageFont.truetype('arial.ttf', 24)
    flb = ImageFont.truetype('arial.ttf', 12)
except:
    ft = fb = fl = fs = fst = flb = ImageFont.load_default()

title = 'Architecture Diagram'
bbox = draw.textbbox((0,0), title, font=ft)
draw.text((cx+cw//2-(bbox[2]-bbox[0])//2, cy+50), title, fill=hex_rgb(COLORS['primary']), font=ft)

# 徽章
draw.rounded_rectangle([cx+cw-120, cy+30, cx+cw-20, cy+54], radius=12, fill=hex_rgb(COLORS['white']), outline=hex_rgb(COLORS['secondary_lighter']))
draw.text((cx+cw-110, cy+36), 'ArchiMate 3.2', fill=hex_rgb(COLORS['primary']), font=fb)

# 四层架构
layers = [
    ('Business Layer', 'Business Role, Process, Service, Object', '#F4B942'),
    ('Application Layer', 'Application Component, Service, Interface', '#66BB6A'),
    ('Data Layer', 'Data Object, Service, Database', '#4A9BD9'),
    ('Technology Layer', 'Node, System Software, Infrastructure', '#7CB342')
]

for i, (name, desc, color) in enumerate(layers):
    y = cy + 130 + i * 90
    draw.rounded_rectangle([cx+40, y, cx+cw-40, y+70], radius=12, fill=hex_rgb(COLORS['white']), outline=hex_rgb(COLORS['secondary_lighter']))
    draw.rectangle([cx+40, y, cx+44, y+70], fill=hex_rgb(color))
    draw.ellipse([cx+56, cy+142+i*90, cx+104, cy+190+i*90], fill=hex_rgb(color))
    draw.text((cx+90, y+24), name, fill=hex_rgb(COLORS['text']), font=fl)
    draw.text((cx+90, y+50), desc, fill=hex_rgb(COLORS['text_secondary']), font=fs)

# 统计
stats = [('100+', 'Elements'), ('25+', 'Viewpoints'), ('7', 'Layers')]
sw = (cw-80) // 3
for i, (v, l) in enumerate(stats):
    sx = cx + 40 + i * sw
    bbox = draw.textbbox((0,0), v, font=fst)
    draw.text((sx+sw//2-(bbox[2]-bbox[0])//2, cy+490), v, fill=hex_rgb(COLORS['primary']), font=fst)
    bbox = draw.textbbox((0,0), l, font=flb)
    draw.text((sx+sw//2-(bbox[2]-bbox[0])//2, cy+522), l, fill=hex_rgb(COLORS['text_secondary']), font=flb)

# 网络装饰节点
random.seed(42)
for i in range(30):
    a = i/30 * 2*math.pi
    d = random.uniform(50, 150)
    x = 200 + d*math.cos(a)
    y = HEIGHT-150 + d*math.sin(a)
    draw.ellipse([x-3, y-3, x+3, y+3], fill=hex_rgb(COLORS['primary_lighter']))

output = 'architecture-diagram.jpg'
img.save(output, 'JPEG', quality=95)
print(f'图片已保存: {os.path.abspath(output)}')
