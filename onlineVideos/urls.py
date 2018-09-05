""" 
@author: glmgracy 
@file:   urls.py 
@time:   2018/09/04 下午10:47
"""
from django.contrib import admin
from django.urls import path
from onlineVideos.views import *

urlpatterns = [
    path('', index, name='index'),
]
