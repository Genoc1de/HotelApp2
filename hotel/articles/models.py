from django.conf import settings
from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name = "Заголовок")
    body = models.TextField(verbose_name = "Основное поле")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=140)


    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('article_list')