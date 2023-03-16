# Posui

`posui` is a python package to extract blog information, tags and images from most of Korean blog platforms.
It supports collecting information from Naver blog, Daum Blog, Tistory and Egloos.

## Installation
```
pip install git+https://github.com/mike3dk/posui
```

## Usage
1. info
```
blog_url = 'https://blog.naver.com/user'

info = posui.info(blog_url)
print(info)

```
2. tags and images
```
blog_url = 'https://blog.naver.com/
tags, images = posui.tags_images(blog_url)
print(tags, images)
```
