"""
@author: glmgracy
@file:   spiders.py
@time:   2018/09/05 下午10:34
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


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
        soup = BeautifulSoup(html, 'lxml')
        title = soup.title.text
        meta_description = ""
        meta_keywords = ""
        print(title)
        metas = soup.find('head').find_all('meta')
        print(metas)
        print('--'*40)
        for i in metas:
            # print(str(i))
            if 'keywords' in str(i):
                meta_keywords = i.attrs['content']
            elif 'description' in str(i):
                meta_description = i.attrs['content']

        print(meta_description, meta_keywords)
        # _ = soup.find(id='topInfo') #.find_all("div")
        _ = soup.find_all('div', class_='info')
        print(_)


spider = Spiders("http://tv.sohu.com/s2014/dsjdecrswsj/")
html = spider.get_html()
spider.get_movie_cover(html)


