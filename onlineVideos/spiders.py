"""
@author: glmgracy
@file:   spiders.py
@time:   2018/09/05 下午10:34
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import etree
from .models import Movies
from django.utils.timezone import now
from decimal import Decimal


class Spiders:
    url = ""

    def __init__(self, url):
        self.url = url
        pass

    def get_html(self):
        response = urlopen(self.url)
        html = response.read().decode('GBK')
        return html

    def get_movie_cover(self, html):
        html = etree.HTML(html)
        title = html.xpath('/html/head/title/text()')[0]
        meta_description = html.xpath('/html/head/meta[2]')[0].attrib["content"]
        meta_keywords = html.xpath('/html/head/meta[3]')[0].attrib["content"]

        return title, meta_description, meta_keywords



spider = Spiders("http://tv.sohu.com/s2014/dsjdecrswsj/")
html = spider.get_html()
title, meta_description, meta_keywords = spider.get_movie_cover(html)