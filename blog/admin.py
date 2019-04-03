from django.contrib import admin
from .models import Writer, Artist, Videos, Music, News, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'slug', 'post' ]
    prepopulated_fields = {'slug': ('title',)}
    date_hierarcy = 'Published'
    search_fields = ['title',]

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
  list_display = ['first_name', 'surname', 'stage_name', 'record_Label']
  search_fields =['stage_name']

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
  list_display = ['title', 'video']
  search_fields = ['title', 'artist']

@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
  list_display = ['first_name', 'surname']

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
  list_display = ['title', 'artist_name', 'release_date', 'music']
  search_fields = ['title', 'artist_name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display =['name', 'body', 'news', 'email']
  search_fields = ['created', 'name', 'news']
