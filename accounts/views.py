from django.shortcuts import redirect, render
from accounts.models import Profile
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
    return render(
        request,
        'profile.html',
        {
            'user': user,
            'profile': profile,
            'connected': connected,
            'discord': username,
        })


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
