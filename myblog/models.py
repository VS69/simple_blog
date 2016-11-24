# coding: utf-8

from __future__ import unicode_literals
from django.db import models


class Post(models.Model):
    # Заголовок поста
    title = models.CharField(max_length=255)

    # Дата публікації
    datetime = models.DateTimeField(u'Дата публікації')

    # Текст поста
    content = models.TextField(max_length=10000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id
