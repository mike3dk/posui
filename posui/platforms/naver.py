from urllib.parse import urlparse
from posui.platforms.common import fetch_soup


def mobile_url(web_url):
    parsed = urlparse(web_url)
    return f"{parsed.scheme}://m.{parsed.netloc}{parsed.path}"


def clean_image(url):
    parsed = urlparse(url)
    server = (
        "postfiles.pstatic.net"
        if parsed.netloc == "mblogthumb-phinf.pstatic.net"
        else parsed.netloc
    )
    query = "type=w966" if parsed.query == "type=w80_blur" else ""
    cleaned = f"{parsed.scheme}://{server}{parsed.path}?{query}"
    return cleaned


def naver_func(web_url):
    url = mobile_url(web_url)

    soup = fetch_soup(url)

    main = soup.select_one("div.post_ct")
    images = [clean_image(i.get("src")) for i in main.select("img")]

    tag_area = soup.select_one("div.post_tag")
    tags = sorted([i.text.replace("#", "") for i in tag_area.select("span")])

    return tags, images
