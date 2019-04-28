from setuptools import setup
from setuptools import find_packages

from img2img import version


setup(
    name="img2img",
    version=version.VERSION,
    author="Ailln",
    author_email="kinggreenhall@gmail.com",
    url="https://github.com/HaveTwoBrush/img2img",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open("./requirements.txt", "r", encoding="utf-8").read().splitlines(),
    description="Convert image format.",
    long_description=open("./README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "jpg2png=img2img:jpg2png"
        ]
    },
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
