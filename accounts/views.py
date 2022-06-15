from django.dispatch import receiver
from django.shortcuts import redirect, render
from accounts.models import Profile
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from allauth.account.signals import user_signed_up


@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    k = SocialAccount.objects.filter(user=request.user)
    if len(k) > 0:
        connected = True
        username = f"{k[0].extra_data['username']}#{k[0].extra_data['discriminator']}"
    else:
        connected = False
        username = None
    if request.GET.get('profile_saved') == "True":
        toast = True
    else:
        toast = False
    return render(
        request,
        'profile.html',
        {
            'user': user,
            'profile': profile,
            'connected': connected,
            'discord': username,
            'toast': toast,
        })


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


@login_required
def save_profile(request):
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
    base_url = reverse('profile')
    url = '{}?profile_saved=True'.format(base_url)
    return redirect(url)


def public_profile(request, username):
    usern = User.objects.get(username=username)
    print(usern)
    profile = Profile.objects.get(user=usern)
    return render(
        request,
        'public_profile.html',
        {'usern': usern, 'profile': profile})


@login_required
def connect(request):
    profile = Profile.objects.get(user=request.user)
    sa = SocialAccount.objects.get(user=request.user)
    profile.discord_id = sa.uid
    profile.avatar_url = sa.get_avatar_url()
    profile.save()
    return redirect('profile')


@receiver(user_signed_up)
def send_discord_webhook(sender, **kwargs):
    pass
