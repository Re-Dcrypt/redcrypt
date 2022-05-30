from django.contrib import admin
from .models import Profile, IPs


class IPsAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address',)
    list_filter = ('count',)
    list_display = [
        'ip_address',
        'count']


admin.site.register(Profile)
admin.site.register(IPs, IPsAdmin)
