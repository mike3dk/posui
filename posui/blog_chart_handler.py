from enum import Enum
from urllib.parse import urlparse

import feedparser

from posui.platforms.common import fetch_soup


class BlogChartHandler:
    def __init__(self, themes):
        self._themes = themes
        self._ranks = self.__find_ranks(self._themes)

    @property
    def ranks(self):
        return self._ranks

    def __find_ranks(self, themes):
        URL = "https://www.blogchart.co.kr/chart/theme"

        soup = fetch_soup(URL)
        found = soup.select("ul.theme_list li a")
        all_themes = [
            {"theme": row.select_one("p").text, "url": row.get("href")} for row in found
        ]

        ranks = {}
        for row in all_themes:
            if row["theme"] not in themes:
                continue

            url = row["url"]
            ranks[row["theme"]] = self.__ranks(url)

        return ranks

    def __ranks(self, url):
        soup = fetch_soup(url)

        list_area = soup.select_one("div.all_category")
        ranks = (
            [row.get("href") for row in list_area.select("table tr td a")]
            if list_area
            else []
        )

        return ranks
