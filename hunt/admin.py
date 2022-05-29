from django.contrib import admin
from .models import AnswerAttempt, LevelTracking, Question, AdditionalHint
# Register your models here.


class AnswerAttemptAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)
    list_filter = ('level', 'user')
    list_display = [
        'answer',
        'level',
        'user',
        'time']


class LevelTrackingAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)
    list_filter = ('level', 'user')


admin.site.register(LevelTracking, LevelTrackingAdmin)
admin.site.register(AnswerAttempt, AnswerAttemptAdmin)
admin.site.register(Question)
admin.site.register(AdditionalHint)
