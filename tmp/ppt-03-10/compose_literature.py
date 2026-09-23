from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / '论文 PPT' / '生成图片_P03-P10_20260923'
SRC = ROOT / '论文 PPT' / '答辩PPT配图-20页版'
BASE = Image.open(OUT / 'P03_运行过程.png').convert('RGB')
W, H = BASE.size
NAVY = (25, 51, 96)
FONT = '/System/Library/Fonts/STHeiti Medium.ttc'


def font(size):
    return ImageFont.truetype(FONT, size)


def fit(path, box):
    im = Image.open(path).convert('RGB')
    max_w, max_h = box[2] - box[0], box[3] - box[1]
    im.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
    x = box[0] + (max_w - im.width) // 2
    y = box[1] + (max_h - im.height) // 2
    return im, (x, y)


def blank(title, number):
    im = Image.new('RGB', (W, H), 'white')
    im.paste(BASE.crop((48, 36, 170, 110)), (48, 36))
    im.paste(BASE.crop((1330, 28, 1652, 110)), (1330, 28))
    d = ImageDraw.Draw(im)
    d.text((68, 139), title, font=font(59), fill=NAVY)
    d.text((70, 232), '02 国内外研究综述', font=font(32), fill=NAVY)
    d.line((101, 891, 1635, 891), fill=NAVY, width=2)
    d.text((40, 870), str(number).zfill(2), font=font(28), fill=NAVY)
    return im


def paste_figure(im, path, box):
    src, pos = fit(path, box)
    im.paste(src, pos)


def label(im, xy, value, size=27):
    ImageDraw.Draw(im).text(xy, value, font=font(size), fill=NAVY)


im = blank('程序调试中的信息查找与原因理解', 8)
paste_figure(im, SRC / 'P08_Whyline_Fig1_从输出提问.png', (61, 310, 806, 775))
paste_figure(im, SRC / 'P08_Whyline_Fig2_原因回溯界面.png', (865, 310, 1610, 775))
label(im, (170, 790), '从异常输出提出问题')
label(im, (1015, 790), '回查相关执行事件')
label(im, (69, 845), '来源：Ko 与 Myers，2009，Whyline，Fig. 1—2', 20)
im.save(OUT / 'P08_程序调试研究.png', quality=95)

im = blank('智能体开发者已有困难', 9)
label(im, (92, 294), '长轨迹检查与消息浏览', 26)
label(im, (972, 294), '识别错误、尝试修复', 26)
paste_figure(im, ROOT / '论文 PPT' / '答辩PPT配图' / '11_AGDebugger完整界面.png', (55, 332, 845, 808))
paste_figure(im, SRC / 'P09_AGDebugger_Fig2_识别错误与尝试修复.png', (884, 332, 1610, 490))
paste_figure(im, SRC / 'P12_AGDebugger_Fig4_编辑与回退.png', (884, 518, 1610, 815))
label(im, (69, 845), '来源：Epperson 等，2025，AGDebugger，Fig. 2—4；相关实践研究见选题报告', 20)
im.save(OUT / 'P09_智能体开发者研究.png', quality=95)

im = blank('运行追踪与自动归因', 10)
paste_figure(im, SRC / 'P10_AgentSight_Fig1_跨层运行环境.png', (85, 312, 730, 800))
paste_figure(im, ROOT / 'tmp' / 'ppt-script' / 'extracted' / 'agentsight-fig2.png', (852, 312, 1497, 800))
label(im, (273, 805), '跨层运行环境', 27)
label(im, (1078, 805), '关联分析组件', 27)
label(im, (69, 845), '来源：Zheng 等，AgentSight，Fig. 1—2；自动归因仅提供检查线索', 20)
im.save(OUT / 'P10_运行追踪与自动归因.png', quality=95)
