# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 800
def h2r(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))

c = {'p':'#1A3A5C', 'pll':'#4A9BD9', 'sl':'#E8F4FC', 'w':'#FFFFFF', 't':'#2D3748', 'ts':'#4A5568'}

img = Image.new('RGB', (W, H), h2r(c['w']))
d = ImageDraw.Draw(img, 'RGBA')

# 背景渐变
for y in range(H):
    r = 255 + int((232-255) * y/H)
    g = 255 + int((244-255) * y/H)
    b = 255 + int((252-255) * y/H)
    d.line([(0,y), (W,y)], fill=(r,g,b))

# 主容器
cx, cy, cw, ch = 100, 80, 1000, 640
d.rounded_rectangle([cx+8, cy+8, cx+cw+8, cy+ch+8], radius=20, fill=h2r(c['sl']))
d.rounded_rectangle([cx, cy, cx+cw, cy+ch], radius=20, fill=h2r(c['w']), outline=h2r(c['sl']), width=2)

ft = ImageFont.load_default()

# 标题
d.text((cx+cw//2-150, cy+50), 'Architecture Diagram', fill=h2r(c['p']), font=ft)

# 徽章
d.rounded_rectangle([cx+cw-120, cy+30, cx+cw-20, cy+54], radius=12, fill=h2r(c['w']), outline=h2r(c['sl']))
d.text((cx+cw-110, cy+36), 'ArchiMate 3.2', fill=h2r(c['p']), font=ft)

# 四层架构
layers = [
    ('Business Layer', 'Business Role, Process, Service, Object', '#F4B942'),
    ('Application Layer', 'Application Component, Service, Interface', '#66BB6A'),
    ('Data Layer', 'Data Object, Service, Database', '#4A9BD9'),
    ('Technology Layer', 'Node, System Software, Infrastructure', '#7CB342')
]

for i, (name, desc, col) in enumerate(layers):
    y = cy + 130 + i * 90
    d.rounded_rectangle([cx+40, y, cx+cw-40, y+70], radius=12, fill=h2r(c['w']), outline=h2r(c['sl']))
    d.rectangle([cx+40, y, cx+44, y+70], fill=h2r(col))
    d.ellipse([cx+56, cy+142+i*90, cx+104, cy+190+i*90], fill=h2r(col))
    d.text((cx+90, y+24), name, fill=h2r(c['t']), font=ft)
    d.text((cx+90, y+50), desc, fill=h2r(c['ts']), font=ft)

# 统计
stats = [('100+', 'Elements'), ('25+', 'Viewpoints'), ('7', 'Layers')]
sw = (cw-80) // 3
for i, (v, l) in enumerate(stats):
    sx = cx + 40 + i * sw
    d.text((sx+sw//2-30, cy+490), v, fill=h2r(c['p']), font=ft)
    d.text((sx+sw//2-40, cy+522), l, fill=h2r(c['ts']), font=ft)

# 保存
output = 'architecture-diagram.jpg'
img.save(output, 'JPEG', quality=95)
print(f'Saved: {os.path.abspath(output)}')
