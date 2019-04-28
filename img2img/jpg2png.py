import os
import sys

from PIL import Image

def save(): 
    len_argv = len(sys.argv)
    if len_argv == 1:
        raise Exception(u"请在 jpg2png 后输入需要转化的图片路径！")
    elif len_argv == 2:
        origin_path = sys.argv[1]
    else:
        raise Exception(u"jpg2png 后的参数过多！")

    img = Image.open(origin_path)

    save_path = os.path.splitext(origin_path)[0] + ".png"
    img.save(save_path)

    print(f"save image in: {save_path}")