from django.contrib import admin

from .models import RedditLinks


class RedditLinksAdmin(admin.ModelAdmin):
	fields = ['title_text', 'pub_date', 'link', 'data_fullname']
	list_display = ('title_text', 'pub_date')
	list_filter = ['pub_date']

admin.site.register(RedditLinks, RedditLinksAdmin)
