"All url views for Bot API"
import json
import os
import threading
from django.http import HttpResponse, JsonResponse
from accounts.models import Profile
from hunt.models import EasterEgg
from django.core.exceptions import ObjectDoesNotExist
from hunt.utils import get_rank, update_rank_all
from sentry_sdk import capture_exception
from django.views.decorators.csrf import csrf_exempt

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
        data_dict['avatar_url'] = user.avatar_url
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


def leaderboard(request):
    "API for getting leaderboard"
    if request.headers.get('Authorization') != os.getenv('API_Authorization'):
        return HttpResponse(status=403)
    try:
        users = Profile.objects.all().exclude(is_banned=True).exclude(
            user__is_staff=True).order_by(
                '-score',
                'last_completed_time')
        data_dict = []
        for user in users[:10]:
            rank = get_rank(user.user)
            if user.discord_id:
                data_dict.append({
                    'username': user.user.username,
                    'score': user.score,
                    'current_level': user.current_level,
                    'rank': rank,
                    'discord_id': user.discord_id
                })
            else:
                data_dict.append({
                    'username': user.user.username,
                    'current_level': user.current_level,
                    'score': user.score, 'rank': rank})
        return HttpResponse(json.dumps(data_dict))
    except Exception as e:
        capture_exception(e)
        return HttpResponse(status=500)


def stats(request, discord_id):
    "API for getting stats"
    if request.headers.get('Authorization') != os.getenv('API_Authorization'):
        return HttpResponse(status=403)
    try:
        user = Profile.objects.get(discord_id=discord_id)
        data_dict = {}
        data_dict['username'] = user.user.username
        data_dict['score'] = user.score
        data_dict['current_level'] = user.current_level
        data_dict['stats'] = user.stats
        data_dict['avatar_url'] = user.avatar_url
        return HttpResponse(json.dumps(data_dict))
    except ObjectDoesNotExist:
        return HttpResponse(status=404)
    except Exception as e:
        capture_exception(e)
        return HttpResponse(status=500)


@csrf_exempt
def ban(request, discord_id, reason):
    "API for banning user"
    if request.headers.get('Authorization') != os.getenv('API_Authorization'):
        return HttpResponse(status=403)
    try:
        user = Profile.objects.get(discord_id=discord_id)
        user.is_banned = True
        user.banned_reason = reason
        user.save()
        return HttpResponse(status=200)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)
    except Exception as e:
        capture_exception(e)
        return HttpResponse(status=500)


@csrf_exempt
def unban(request, discord_id):
    "API for unbanning user"
    if request.headers.get('Authorization') != os.getenv('API_Authorization'):
        return HttpResponse(status=403)
    try:
        user = Profile.objects.get(discord_id=discord_id)
        user.is_banned = False
        user.save()
        return HttpResponse(status=200)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)
    except Exception as e:
        capture_exception(e)
        return HttpResponse(status=500)


@csrf_exempt
def easteregg(request, discord_id, egg):
    "API for easter egg"
    if request.headers.get('Authorization') != os.getenv('API_Authorization'):
        return HttpResponse(status=403)
    try:
        user = Profile.objects.get(discord_id=discord_id)
        try:
            egg = EasterEgg.objects.get(egg=egg)
            if egg.claimed:
                return JsonResponse(
                    {
                        'code': 'claimed',
                        'response': "This egg has already been claimed"}
                    )
            else:
                egg.claimed = True
                egg.claimed_by = user.user
                user.score += egg.points
                user.save()
                egg.save()
                return JsonResponse(
                    {
                        'code': 'success',
                        'response': f"Congrats! You have claimed this egg. Added {egg.points} points to your score."})
        except ObjectDoesNotExist:
            return JsonResponse({
                'code': 'not_found',
                'response': 'Wrong! Try again!'})
        except Exception as e:
            capture_exception(e)
            return HttpResponse(status=500)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)
    except Exception as e:
        capture_exception(e)
        return HttpResponse(status=500)


@csrf_exempt
def update_rank(request):
    "API for updating rank"
    print(request.headers.get('Authorization')+"=="+os.getenv('API_Authorization'))
    if request.headers.get('Authorization') != os.getenv('API_Authorization'):
        return HttpResponse(status=403)
    t = threading.Thread(target=update_rank_all, args=(), kwargs={})
    t.start()
    return JsonResponse({'status': "Updating"}, status=200)
