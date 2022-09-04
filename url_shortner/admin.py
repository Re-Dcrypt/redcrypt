from django.contrib import admin
from .models import UrlShortner
# Register your models here.


class UrlShortnerAdmin(admin.ModelAdmin):
    list_display = [
        'short_url',
        'full_url',
        'click_counts',
        'active',
    ]
    readonly_fields = ['visited_by']

    def reset_click_counts(self, request, queryset):
        queryset.update(click_counts=0)
        self.message_user(
            request, f"Resetted click counts for {queryset.count()} Url(s)"
            )

    def make_active(self, request, queryset):
        queryset.update(active=True)
        self.message_user(
            request, f"Activated {queryset.count()} Url(s)"
            )
    
    def make_inactive(self, request, queryset):
        queryset.update(active=False)
        self.message_user(
            request, f"Deactivated {queryset.count()} Url(s)"
            )

    reset_click_counts.short_description = "Reset click counts"
    make_active.short_description = "Activate Url(s)"
    make_inactive.short_description = "Deactivate Url(s)"

    actions = [reset_click_counts, make_active, make_inactive]


admin.site.register(UrlShortner, UrlShortnerAdmin)
