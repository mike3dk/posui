from enum import Enum


class BlogType(Enum):
    NAVER = 1
    DAUM = 2
    TISTORY = 3
    EGOOLS = 4


def detect_type(url):
    blog_type = BlogType.NAVER
    return blog_type
