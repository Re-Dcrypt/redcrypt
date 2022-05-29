"All url views for Bot API"
import json
from django.http import HttpResponse
from accounts.models import Profile
# Create your views here.


def get_profile(request, discord_id):
    "API for getting profile"
    user = Profile.objects.get(discord_id=discord_id)
    dict = {}
    dict['username'] = user.user.username
    if user.is_banned:
        dict["ban"] = True
        if user.banned_reason:
            dict["banned_reason"] = user.banned_reason
        else:
            dict["banned_reason"] = "Banned"
        return HttpResponse(json.dumps(dict))
    if user.is_public_name:
        dict['name'] = user.name
    dict['score'] = user.score
    dict['current_level'] = user.current_level
    if user.is_public_organization:
        dict['organization'] = user.organization
    return HttpResponse(json.dumps(dict))
