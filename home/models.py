from django.db import models

# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=30, verbose_name="이름")
    content = models.TextField(verbose_name="댓글")
    created_at = models.DateField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateField(auto_now_add=True, verbose_name="수정일")