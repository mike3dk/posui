#!/usr/bin/env python3
from distutils.core import setup

setup(
    name="posui",
    version="1.0.0",
    description="extract info, tag and images from blog",
    author="mike3dk",
    install_requires=["requests", "beautifulsoup4", "feedparser", "pyyaml"],
    python_requires=">=3.6",
    packages=["posui", "posui/platforms"],
)
