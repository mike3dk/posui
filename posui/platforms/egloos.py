from urllib.parse import urlparse

import feedparser

from posui.platforms.common import fetch_soup


def egloos_func_blog_info(rss_url):
    parsed = feedparser.parse(rss_url)
    info = {
        "title": parsed.feed.title,
        "url": parsed.feed.link,
        "rss_url": rss_url,
        "description": parsed.feed.description,
        "image": parsed.feed.image.href,
    }
    return info


def clean_image(url):
    return url


def clean_tag(tag_text):
    return tag_text


def egloos_func_tags_images(url):
    soup = fetch_soup(url)

    main = soup.select_one("div.hentry")
    images = [clean_image(img.get("src")) for img in main.select("img")]

    tag_area = soup.select_one("div.post_taglist")
    tags = sorted([clean_tag(tag.text) for tag in tag_area.select("a[rel='tag']")])

    return tags, images
