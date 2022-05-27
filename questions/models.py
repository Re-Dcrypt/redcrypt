from django.db import models
from django.contrib import admin


class Question(models.Model):
    unique_name = models.CharField(max_length=255, null=True, blank=True)
    answer = models.CharField(max_length=255)
    is_custom_template = models.BooleanField(default=False)
    img_url = models.URLField(blank=True, null=True)
    question_text = models.TextField(blank=True, null=True)
    level = models.IntegerField(default=0)



class AdditionalHint(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    hint_text = models.CharField(max_length=1024)


admin.site.register(Question)
admin.site.register(AdditionalHint)
