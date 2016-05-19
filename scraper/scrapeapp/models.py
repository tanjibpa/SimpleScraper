# from __future__ import unicode_literals

from django.db import models

class RedditLinks(models.Model):
    title_text = models.TextField()
    link = models.TextField()
    pub_date = models.DateTimeField()
    data_fullname = models.CharField(max_length=20)

    def __str__(self):
    	return self.title_text
