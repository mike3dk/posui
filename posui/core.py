from urllib.parse import urlparse

import feedparser

from posui.type_detector import detect_type
from posui.platforms.naver import naver_func

# from posui.platforms.daum import daum_func
# from posui.platforms.tistory import tistory_func
# from posui.platforms.egloos import egloos_func
from posui.type_detector import BlogType

type_func_dict = {
    "Naver Blog": naver_func,
    # BlogType.DUAM: daum_func,
    # BlogType.TISTORY: tistory_func,
    # BlogType.EGOOLS: egloos_func,
}


class Posui:
    def __init__(self, url):
        self._url = url
        self._rss_url = self.__guess_rss_url(url)
        self._blog_info = self.__extract_blog_info(self._rss_url)
        func = type_func_dict[self._blog_info["generator"]]
        self._tags, self._images = func(url)

    @property
    def blog_info(self):
        return self._blog_info

    @property
    def post_tags_images(self):
        return self._tags, self._images

    def __guess_rss_url(self, url):
        parsed = urlparse(url)
        parts = parsed.path.split("/")
        path_parts = [part for part in parts if part]

        if parsed.netloc == "blog.naver.com":
            name = path_parts[0]
            return f"http://rss.{parsed.netloc}/{name}.xml"

        if parsed.netloc == "daum.net":
            return f"http://blog.daum.net/xml/rss{parsed.path}"

        name = parsed.path.split(".")[0]
        if parsed.netloc == "egloos.com":
            return f"http://rss.egloos.com/blog/{name}"

        if parsed.netloc == "blog.me":
            return f"http://rss.blog.naver.com/{name}.xml"

        return f"http://{parsed.netloc}/rss"

    def __extract_blog_info(self, url):
        parsed = feedparser.parse(url)

        info = {
            "title": parsed.feed.title,
            "url": parsed.feed.link,
            "rss_url": url,
            "image": parsed.feed.image.href,
            "description": parsed.feed.description,
            "generator": parsed.feed.generator,
        }

        return info
