from django.db import models
from django.db.models.base import Model

# Create your models here.

class Todo(models.Model):

  title = models.CharField('タイトル', max_length=55)
  body = models.TextField('詳細/内容', max_length=200)
  created = models.DateTimeField('作成日時', auto_now_add=True)
  updated = models.DateTimeField('更新日時', auto_now=True)
  
  def __str__(self):
      return self.title