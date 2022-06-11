from django import template
from accounts.models import Profile


register = template.Library()


@register.simple_tag(name="avatar")
def avatar(user):
    profile = Profile.objects.get(user=user)
    return profile.avatar_url
