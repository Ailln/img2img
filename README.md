# img2img: Image to Image

🔮快速转化图片格式

[![](https://award.dovolopor.com?lt=language&rt=Py36&rbc=pink)](https://docs.python.org/3.6/)
[![](https://award.dovolopor.com?lt=PyPI&rt=0.1.2)](https://pypi.org/project/img2img/)
[![](https://award.dovolopor.com?lt=Ailln's&rt=idea&lbc=lightgray&rbc=red&ltc=red)](https://github.com/Ailln/award)

> **🚨更新日志：**
>
> - `v0.0.1` 初始化项目，添加在命令行使用 jpg2png 方法；
> - `v0.1.0` 添加常见的 6 种转化方法；
> - `v0.1.1` 修复版本错误问题；
> - `v0.1.2` 回保存图片的路径；
> - `v0.2.0` 支持命令行批量转化。

## 1 功能

1. 支持 **6 种**常见图片格式转化；
2. 支持在**命令行**调用；
3. 支持在[**网页上**](https://www.dovolopor.com/img2img)使用。

![](./src/img2img-site.png)
🔗[点我访问](https://www.dovolopor.com/img2img)

## 2 安装

### 2.1 使用 pip 安装

```shell
pip install img2img
```

### 2.2 从代码库安装

```shell
git clone https://github.com/Ailln/img2img.git
cd img2img
python setup.py install
```

## 3 使用

目前总共支持6种方法，如下：

1. jpg2png
2. png2jpg
3. jpg2ico
4. ico2jpg
5. png2ico
6. ico2png

下文中使用 `jpg2png` 作为演示，其他方法同理。

### 3.1 在代码中调用

```python
# 在文件首部引入包
import img2img

# 查看版本
img2img.__version__
# output: 0.2.0

img = img2img.Img2img()

# 默认输出路径和输入路径相同
img.convert("jpg2png", "./test.jpg")

# 支持手动修改输出路径
img.convert("jpg2png", "./test.jpg", "../new_test.png")
```

### 3.2 在命令行中使用

```bash
# 默认输出路径和输入路径相同
jpg2png ./test.jpg

# 支持手动修改输出路径
jpg2png ./test.jpg ../new_test.png

# 支持文件夹批量转化
jpg2png ./test/
```

## 4 版本支持

- 理论上支持 `Windows`、`MacOS`、`Ubuntu` 下的所有 `Python 3.6` 的版本。
- 实际上仅在 `Windows 10`、`MacOS 10.14`、`Ubuntu 16.04` 的 `Python 3.6.3` 上做过完整测试。
- 欢迎提交其他版本使用情况到 [Issues](https://github.com/Ailln/img2img/issues) 中，期待你的反馈。
- 如果你有 `Python 2` 的使用需求，可 Fork 代码自行修改。当然也欢迎提 PR，贡献自己代码给其他人。

## 5 协议

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)

## 6 参考

- [如何发布自己的包到 pypi ？](https://www.v2ai.cn/python/2018/07/30/PY-1.html)
- [python 中的小陷阱](https://www.v2ai.cn/python/2019/01/01/PY-6.html)