from django.contrib import admin
from .models import AnswerAttempt, LevelTracking, Question, AdditionalHint, SampleQuestion
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
    list_display = ['user', 'level']


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


class SampleQuestionAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'answer',
        'level',
        'points',
    ]


admin.site.register(LevelTracking, LevelTrackingAdmin)
admin.site.register(AnswerAttempt, AnswerAttemptAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(AdditionalHint, AdditionalHintAdmin)
admin.site.register(SampleQuestion, SampleQuestionAdmin)
