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


class QuestionAdmin(admin.ModelAdmin):
    ordering = ['level']
    list_display = [
        'short_name',
        'level',
    ]
    fieldsets = (
        ('Details',
            {'fields': [
                ('short_name', 'is_custom_template'),
                ('level', 'points'),
            ]}),
        ('Question',
            {'fields': [
                ('question_text', 'answer'),
                ('img_url',)
            ]})
    )


class AdditionalHintAdmin(admin.ModelAdmin):
    list_display = [
        'hint_text',
        'level',
    ]

    def level(self, obj):
        return obj.question.level


admin.site.register(LevelTracking, LevelTrackingAdmin)
admin.site.register(AnswerAttempt, AnswerAttemptAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(AdditionalHint, AdditionalHintAdmin)
