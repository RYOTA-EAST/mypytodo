from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils import timezone
import datetime

# Create your models here.

class Todo(models.Model):
  STATUS_CHOICES = [(1, '未着手'),(2, '作業中'),(3, '完   了')]

  title = models.CharField('タイトル', max_length=55)
  body = models.TextField('詳細/内容', max_length=200)
  status = models.IntegerField(choices=STATUS_CHOICES, default=1)
  deadline = models.DateTimeField('期限', default=timezone.now)
  created = models.DateTimeField('作成日時', auto_now_add=True)
  updated = models.DateTimeField('更新日時', auto_now=True)
  create_user = models.ForeignKey(get_user_model(), on_delete=CASCADE, default=1)
  
  def publish(self):
    self.update_at = timezone.now()
    self.save()
  
  def __str__(self):
      return self.title

  def deadline_flag(self):
    today = timezone.now()
    if self.deadline < today:
      return 0
    elif self.deadline <= today + datetime.timedelta(days=3):
      return 1
    else:
      return 2