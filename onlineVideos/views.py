from django.shortcuts import render
from django.http import HttpResponse
from .spiders import Spiders
from .models import Movies
from django.utils.timezone import now
from decimal import Decimal
# Create your views here.


def index(request):
    spider = Spiders("http://tv.sohu.com/s2014/dsjdecrswsj/")
    html = spider.get_html()
    title, meta_description, meta_keywords = spider.get_movie_cover(html)
    # movies = Movies(title=title,
    #                 director='director',
    #                 stars='Gracy.Ma',
    #                 category='爱情片',
    #                 release_date=now(),
    #                 country='China',
    #                 language='Chinese',
    #                 description='xxxxdesc',
    #                 rate="6.8",
    #                 play_count=5000,
    #                 runtime=150,
    #                 img='http://www.baidu.com/xx.jpg',
    #                 page_title=title,
    #                 page_meta_desc=meta_description,
    #                 page_meta_keywords=meta_keywords
    #                 )
    #
    # movies.save()
    print('ssss')
    return render(request, 'onlineVideos/Index.html')
