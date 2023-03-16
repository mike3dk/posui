# Posui

`posui` is a python package to extract blog information, tags and images from most of Korean blog platforms.
It supports collecting information from Naver blog, Daum Blog, Tistory and Egloos.

## Installation
```
pip install git+https://github.com/mike3dk/posui
```

## Usage
```
blog_url = 'https://blog.naver.com/songsong14/222993193146'

info = posui.info(blog_url)
print(info)
tags, images = posui.tags_images(blog_url)
print(tags, images)
```
