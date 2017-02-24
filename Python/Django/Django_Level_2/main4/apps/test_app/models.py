from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=25)
  last_name = models.CharField(max_length=25)
  age = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.first_name + " " + self.last_name
class Blog(models.Model):
    title = models.CharField(max_length=100)
    blog = models.TextField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    created_at = models.DateField(auto_now=True)

class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    comment = models.TextField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    created_at = models.DateField(auto_now=True)
