import unittest

from .img2img import Img2img


class Img2imgTest(unittest.TestCase):
    def setUp(self) -> None:
        self.input_data = {
            "jpg2png": ["./test/", "./test/vim_skill.jpg"]
        }
        self.img = Img2img()

    def test_convert(self) -> None:
        for item in self.input_data.keys():
            for _path in self.input_data[item]:
                self.img.convert(item, _path)
