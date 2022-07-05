from django.shortcuts import redirect, render
from django.http import JsonResponse
from accounts.models import Profile
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from hunt.decorators import not_banned
from allauth.account.utils import send_email_confirmation
from django.core.exceptions import ObjectDoesNotExist
from hunt.utils import get_rank
from sentry_sdk import capture_exception


@not_banned
@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    k = SocialAccount.objects.filter(user=request.user)
    rank = get_rank(request.user)
    if len(k) > 0:
        connected = True
        username = f"{k[0].extra_data['username']}#{k[0].extra_data['discriminator']}"
    else:
        connected = False
        username = None
    return render(
        request,
        'profile.html',
        {
            'user': user,
            'profile': profile,
            'connected': connected,
            'discord': username,
            'rank': rank,
        })


@not_banned
@login_required
def edit_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    return render(
        request,
        'edit_profile.html',
        {
            'user': user,
            'profile': profile,
        })


@not_banned
@login_required
def save_profile(request):
    if request.method == "POST":
        try:
            user = request.user
            profile = Profile.objects.get(user=user)
            profile.name = request.POST['name']
            try:
                if request.POST['is_name_public'] == "on":
                    profile.is_public_name = True
                else:
                    profile.is_public_name = False
            except KeyError:
                profile.is_public_name = False
            profile.organization = request.POST['organization']
            try:
                if request.POST['is_organization_public'] == "on":
                    profile.is_public_organization = True
                else:
                    profile.is_public_organization = False
            except KeyError:
                profile.is_public_organization = False
            profile.save()
            return JsonResponse({'saved': True}, status=200)
        except Exception as e:
            capture_exception(e)
            return JsonResponse({'saved': False}, status=400)


def public_profile(request, username):
    try:
        usern = User.objects.get(username=username)
        profile = Profile.objects.get(user=usern)
        rank = get_rank(usern)
        return render(
            request,
            'public_profile.html',
            {'usern': usern, 'profile': profile, 'rank': rank})
    except ObjectDoesNotExist:
        return render(request, '404.html', status=404)


@not_banned
@login_required
def connect(request):
    profile = Profile.objects.get(user=request.user)
    sa = SocialAccount.objects.get(user=request.user)
    profile.discord_id = sa.uid
    profile.avatar_url = sa.get_avatar_url()
    profile.save()
    return redirect('profile')


@not_banned
@login_required
def send_confirmation_email(request):
    send_email_confirmation(request, request.user)
    return redirect('verification-sent')


@login_required
def verification_sent(request):
    return render(request, 'verification_sent.html')
