from .. models import News
from django.db.models import Count
from django import template
register = template.Library()

@register.simple_tag
def total_tag():
  return News.objects.count()

@register.inclusion_tag('blog/lastest-gist.html')
def latest_news(count=5):
  latest_gossip = News.objects.order_by('-publish')[:count]
  return {'latest_gossip': latest_gossip} 

#@register.assignment_tag
#def most_read(count=5):
 # 	 return News.objects.annotate(total_comment=Count('comment')).order_by('total_comment')[:count]