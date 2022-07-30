from django.contrib import admin
from .models import UrlShortner
# Register your models here.


class UrlShortnerAdmin(admin.ModelAdmin):
    list_display = [
        'short_url',
        'full_url',
        'click_counts',
    ]
    readonly_fields = ['visited_by']

    def reset_click_counts(self, request, queryset):
        queryset.update(click_counts=0)
        self.message_user(
            request, f"Resetted click counts for {queryset.count()} Url(s)"
            )

    reset_click_counts.short_description = "Reset click counts"

    actions = [reset_click_counts]


admin.site.register(UrlShortner, UrlShortnerAdmin)
