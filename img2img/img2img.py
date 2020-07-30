import os
import sys

from PIL import Image


class Img2img(object):
    def __init__(self):
        self.methods = [
            "jpg2png",
            "png2jpg",
            "jpg2ico",
            "ico2jpg", 
            "png2ico",
            "ico2png"
        ]

    def convert(self, method, input_path, output_path=None):
        if method in self.methods:
            print(f"\n>> start convert: {input_path}")
            input_split_list = os.path.splitext(input_path)
            input_name = input_split_list[0]
            input_type = input_split_list[1]

            method_input_type, method_output_type = method.split("2")
            if input_type[1:] != method_input_type:
                print(f"!! {input_path} can not convert to {method_input_type}")
                return

            if output_path:
                output_split_list = os.path.splitext(output_path)
                output_name = output_split_list[0]
                output_type = output_split_list[1]
                assert(output_type[1:] == method_output_type)
            else:
                output_name = input_split_list[0]
                output_type = "." + method_output_type
        else:
            raise ValueError(f"{method} not allowed !")

        input_path = input_name + input_type
        img = Image.open(input_path)
        if input_type == ".png":
            img = img.convert('RGB')
        output_path = output_name + output_type
        img.save(output_path)
        print(f">> save in: {output_path}")
        return output_path

    def convert_from_shell(self, method):
        if method in sys.argv[0]:
            len_argv = len(sys.argv)
            if len_argv == 1:
                raise Exception(f"请在 {method} 后输入需要转化的图片路径！")
            elif len_argv == 2:
                input_path = sys.argv[1]
                # 判断是文件还是文件夹
                if os.path.isfile(input_path):
                    self.convert(method, input_path)
                elif os.path.isdir(input_path):
                    for _path in os.listdir(input_path):
                        self.convert(method, os.path.join(input_path, _path))
                else:
                    raise Exception(f"输入路径错误: {input_path}")
            elif len_argv == 3:
                input_path = sys.argv[1]
                output_path = sys.argv[2]
                if os.path.isfile(input_path):
                    self.convert(method, input_path, output_path)
                elif os.path.isdir(input_path):
                    for _path in os.listdir(input_path):
                        self.convert(method, os.path.join(input_path, _path), output_path)
                else:
                    raise Exception(f"输入路径错误: {input_path}")
            else:
                raise Exception(f"{method} 后的参数过多！")
    
    def jpg2png(self):
        return self.convert_from_shell("jpg2png")

    def png2jpg(self):
        return self.convert_from_shell("png2jpg")

    def jpg2ico(self):
        return self.convert_from_shell("jpg2ico")

    def ico2jpg(self):
        return self.convert_from_shell("ico2jpg")

    def png2ico(self):
        return self.convert_from_shell("png2ico")

    def ico2png(self):
        return self.convert_from_shell("ico2png")
