from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Question(models.Model):
    "Question Model"
    unique_name = models.CharField(max_length=255, null=True, blank=True)
    answer = models.CharField(max_length=255)
    is_custom_template = models.BooleanField(default=False)
    img_url = models.URLField(blank=True, null=True)
    question_text = models.TextField(blank=True, null=True)
    level = models.IntegerField(default=0)


class AdditionalHint(models.Model):
    "Hint for questions"
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    hint_text = models.CharField(max_length=1024)


class UserProgressAdmin(admin.ModelAdmin):
    readonly_fields = ('last_completed_time',)
    list_filter = ('current_level', 'user')


class LevelTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.IntegerField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ': '.join([str(self.user), str(self.level)])

    class Meta:
        verbose_name_plural = "Level Completion Tracking"


class LevelTrackingAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)
    list_filter = ('level', 'user')


class AnswerAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.IntegerField()
    answer = models.CharField(max_length=1024)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.answer)

    class Meta:
        verbose_name_plural = "Answer Attempts"


class AnswerAttemptAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)
    list_filter = ('level', 'user')
    list_display = [
        'answer',
        'level',
        'user',
        'time']


admin.site.register(LevelTracking, LevelTrackingAdmin)
admin.site.register(AnswerAttempt, AnswerAttemptAdmin)
admin.site.register(Question)
admin.site.register(AdditionalHint)
