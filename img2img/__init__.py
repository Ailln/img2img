from . import version
from . import img2img


__version__ = version.VERSION
Img2img = img2img.Img2img
jpg2png = Img2img().jpg2png
png2jpg = Img2img().png2jpg
jpg2ico = Img2img().jpg2ico
ico2jpg = Img2img().ico2jpg
png2ico = Img2img().png2ico
ico2png = Img2img().ico2png