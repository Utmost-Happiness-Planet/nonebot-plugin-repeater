from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nonebot-plugin-repeater",
    version="2.0.1",
    author="Kl1nge5",
    description="A plugin based on NoneBot2, auto +1 in group.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ninthseason/nonebot-plugin-repeater",
    project_urls={
        "Bug Tracker": "https://github.com/ninthseason/nonebot-plugin-repeater/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=["nonebot_plugin_repeater"],
    python_requires=">=3.7",
    install_requires=[
        "nonebot2 >= 2.0.0b2",
        "nonebot2-adapter-onebot >= 2.0.0b1"
    ]
)
