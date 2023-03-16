from posui.type_detector import detect_type
from posui.platforms.naver import naver_func

# from posui.platforms.daum import daum_func
# from posui.platforms.tistory import tistory_func
# from posui.platforms.egloos import egloos_func
from posui.type_detector import BlogType

type_func_dict = {
    BlogType.NAVER: naver_func,
    # BlogType.DUAM: daum_func,
    # BlogType.TISTORY: tistory_func,
    # BlogType.EGOOLS: egloos_func,
}


class Posui:
    def __init__(self, url):
        self._url = url
        self._info = url
        btype = detect_type(url)
        func = type_func_dict[btype]
        self._tags, self._images = func(url)

    @property
    def info(self):
        return self._info

    @property
    def tags_images(self):
        return self._tags, self._images
