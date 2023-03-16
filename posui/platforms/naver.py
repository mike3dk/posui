from urllib.parse import urlparse
from posui.platforms.common import fetch_soup


def naver_func(url):
    pres = urlparse(url)
    soup = fetch_soup(url)
    iframe_url = soup.select_one("iframe#mainFrame")["src"]

    url2 = f"{pres.scheme}://{pres.netloc}{iframe_url}"
    soup2 = fetch_soup(url2)

    breakpoint()

    images = []
    tags = []

    return images, tags
