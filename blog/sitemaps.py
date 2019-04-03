from django.contrib.sitemaps import Sitemap
from .models import News

class NewSiteMap(Sitemap):
  changefreq = 'weekly'
  priority = 0.9

  def item(self):
  	return News.objects.all()

  def lastmodify(self, obj):
    return obj.publish