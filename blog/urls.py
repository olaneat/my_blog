from . import views
from django.urls import re_path, include, path



urlpatterns = [
    path('', views.index, name = 'index'),
    re_path(r'^/news_detail/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<news>[-\w]+)/$', \
    views.news_detail, name ='news-detail'),
    path('music_list', views.music_detail, name = 'music_list'),
    re_path(r'^(?P<news_id>\d+)/share_news', views.share_post, name ='share-post' )
    #re_path(r'^music/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>\d[-\w]+)/$', views.MusicListView.as_view(), name = "music-detail"),

    #path('news/<slug>', views.NewsDetailView.as_view(), name ='news-detail' )


]
