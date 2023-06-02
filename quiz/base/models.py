from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')

  def children(self):
    return Comment.objects.filter(parent=self).order_by('-created_at').all()
  
  def is_parent(self):
    if self.parent is None:
      return True
    return False