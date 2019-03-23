from django.contrib.syndication.views import Feed
from django.urls import reverse
from myblog.models import Post

class LatestPostFeed(Feed):
    title = 'Latest Posts'
    link = '/'
    description = 'The most recently created  and / or updated posts'

    def items(self):
        published = Post.objects.exclude(published_date__exact=None)
        posts = published.order_by('-published_date')
        return posts

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return f'/posts/{item.id}'