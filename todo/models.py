from django.db import models
from django.db.models.base import Model
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
  STATUS_CHOICES = [(1, '未完了'),(2, '作業中'),(3, '完了')]

  title = models.CharField('タイトル', max_length=55)
  body = models.TextField('詳細/内容', max_length=200)
  status = models.IntegerField(choices=STATUS_CHOICES, default=1)
  deadline = models.DateTimeField('期限', default=timezone.now)
  created = models.DateTimeField('作成日時', auto_now_add=True)
  updated = models.DateTimeField('更新日時', auto_now=True)
  
  def publish(self):
    self.update_at = timezone.now()
    self.save()
  
  def __str__(self):
      return self.title