from django.contrib import admin
from .models import Profile, IPs


class IPsAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address',)
    list_filter = ('count',)
    list_display = [
        'ip_address',
        'count']
    fields = [
        ('users_from_ip', 'count'),
        ('ip_address',)
    ]


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'name', 'discord_id']
    readonly_fields = ('user', 'last_completed_time')
    list_display = [
        'user',
        'score',
        'current_level',
        'ip_address_count'
    ]
    list_filter = ['is_banned', 'ip_address_count', 'current_level']
    fieldsets = (
        ('Details',
            {'fields': [
                ('user'),
                ('name', 'is_public_name'),
                ('organization', 'is_public_organization'),
                ('discord_id'),
                ('avatar_url')
                ]}),
        ('Hunt',
            {'fields': [
                ('score', 'current_level'),
                ('last_completed_time'),
                ('banned_reason', 'is_banned')
                ]}),
        ('IPs',
            {'fields': [
                ('ip_address', 'ip_address_count')
                ]})
    )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(IPs, IPsAdmin)
