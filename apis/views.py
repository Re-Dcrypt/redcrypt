"All url views for Bot API"
import json
import os
from django.http import HttpResponse, JsonResponse
from accounts.models import Profile
from django.core.exceptions import ObjectDoesNotExist
from hunt.utils import get_rank
from sentry_sdk import capture_exception
# Create your views here.


def get_profile(request, discord_id):
    "API for getting profile"
    if request.headers.get('Authorization') != os.getenv('API_Authorization'):
        return HttpResponse(status=403)
    try:
        user = Profile.objects.get(discord_id=discord_id)
        rank = get_rank(user.user)
        data_dict = {}
        data_dict['username'] = user.user.username
        if user.is_banned:
            data_dict["ban"] = True
            if user.banned_reason:
                data_dict["banned_reason"] = user.banned_reason
            else:
                data_dict["banned_reason"] = "Banned"
            return HttpResponse(json.dumps(data_dict))
        if user.is_public_name:
            data_dict['name'] = user.name
        data_dict['score'] = user.score
        data_dict['current_level'] = user.current_level
        data_dict['rank'] = rank
        if user.is_public_organization:
            data_dict['organization'] = user.organization
        return HttpResponse(json.dumps(data_dict))
    except ObjectDoesNotExist:
        return HttpResponse(status=404)


def verify_discord_id(request, discord_id):
    "API for verifying discord id"
    if request.headers.get('Authorization') != os.getenv('API_Authorization'):
        return HttpResponse(status=403)
    try:
        user = Profile.objects.get(discord_id=discord_id)
        return JsonResponse({'Username': user.user.username}, status=200)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)
    except Exception as e:
        capture_exception(e)
        return HttpResponse(status=500)
