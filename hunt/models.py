from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    "Question Model"
    short_name = models.CharField(max_length=255, null=True, blank=True)
    answer = models.CharField(max_length=255)
    is_custom_template = models.BooleanField(default=False)
    img_url = models.URLField(blank=True, null=True)
    question_text = models.TextField(blank=True, null=True)
    level = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.level}: {self.short_name}"


class AdditionalHint(models.Model):
    "Hint for questions"
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    hint_text = models.CharField(max_length=1024)

    def __str__(self):
        return self.hint_text


class LevelTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.IntegerField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ': '.join([str(self.user), str(self.level)])

    class Meta:
        verbose_name_plural = "Level Completion Tracking"


class AnswerAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.IntegerField()
    answer = models.CharField(max_length=1024)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.answer)

    class Meta:
        verbose_name_plural = "Answer Attempts"


class SampleQuestion(models.Model):
    question = models.TextField()
    answer = models.CharField(max_length=255)
    img_url = models.URLField(blank=True, null=True)
    level = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    completed_by = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"{self.level}: {self.question}"

    class Meta:
        verbose_name_plural = "Sample Questions"
