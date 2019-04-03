from django.shortcuts import render, get_object_or_404
from .models import News, Artist, Music, Writer, Videos, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPost, CommentForm
from django.core.mail import send_mail
#from http import HttpResponse
from django.views import generic
# Create your views here.

def index(request):
  news_list = News.objects.all()
  paginator = Paginator(news_list, 10 )
  page = request.GET.get('page')
  try:
    news = paginator.page(page)
  except PageNotAnInteger:
    news = paginator.page(1)
  except EmptyPage:
   news = paginator.page(paginator.num_pages)
  return render(request, 'blog/index.html', 
                {'news': news, 'page': page})


def news_detail(request, year, month, day, news):
  news = get_object_or_404(News, slug = news,\
          publish__year =year,\
          publish__month =month, publish__day = day)
  
  comments = news.comments.filter(active = True)
  if request.method =='POST':
    comment_info = CommentForm(data = request.POST)
    if comment_info.is_valid():
      new_comment = comment_info.save(commit =False)
      new_comment.news = news
      new_comment.save()
  else:
    comment_info = CommentForm()
    context = {'news':news, 'comment_info': comment_info,\
              'comments':comments}
  
  return render(request,'blog/news_detail.html', context)


class MusicListView(generic.ListView):
  model = Music
  template_name = 'blog/music_list.html'
  paginate_by =15

class MusicDetailView(generic.DetailView):
  model = Music
  template_name ='blog/music_detail.html'

def music_detail(request, year, mouth, days):
  music = get_object_or_404(News, slug =post,
                           publish__date = year,
                           publish__month  = month,
                           status = 'published')
  return render(render, 'blog/news-detail.html', {'music': music})


def share_post(request, news_id):
  news = get_object_or_404(News, id = news_id, status = 'published')
  sent = False
  if request.method == 'POST':
    post_form =EmailPost(request.POST)
    if post_form.is_valid():
      cd = post_form.cleaned_data
      post_url = request.build_absolute_uri(news.get_absolute_url())
      subject = '{} ({}) recommend you reading {}'.format(cd['name'], cd['email'], news.title)
      message = 'Read "{}" at {}\n\n{}\'s comments: '.format(news.title,  cd[post])
      send_mail(subject, message, 'admin@myblog.com', [cd[to]])
      sent =True
  else:
    post_form =EmailPost()
  return render(request, 'blog/share_update.html', {'news': news,
                                                    'post_form': post_form,
                                                    'sent': sent })
