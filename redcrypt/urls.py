"""redcrypt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hunt.views import index, offline, play, check_ans, leaderboard, faqs
from accounts import views as accounts_views


urlpatterns = [
    path('', index, name='index'),
    path('', include('pwa1.urls')),
    path('offline/', offline, name="offline"),
    path('offline', offline, name="offline"),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('honeypot/', admin.site.urls),
    path('api/', include(('apis.urls', 'apis'), namespace='api')),
    path(
        'accounts/social/connections/',
        accounts_views.connect, name='connect'),
    path('accounts/', include('allauth.urls')),

    path('profile/', accounts_views.profile, name='profile'),
    path('profile', accounts_views.profile),
    path('profile/edit/', accounts_views.edit_profile, name='edit_profile'),
    path(
        'profile/edit/save_profile',
        accounts_views.save_profile,
        name='save_profile'),
    path(
        'profile/<str:username>/',
        accounts_views.public_profile,
        name='public-profile'),
    path(
        'profile/<str:username>',
        accounts_views.public_profile),
    path(
        'send_confirmation_email',
        accounts_views.send_confirmation_email,
        name='send_confirmation_email'),
    path(
        'verification-sent',
        accounts_views.verification_sent,
        name='verification-sent'),
    path('play/', play, name='play'),
    path('play', play),
    path('leaderboard/', leaderboard, name='leaderboard'),
    path('leaderboard', leaderboard,),
    path('faqs/', faqs, name='faqs'),
    path('faqs', faqs,),
    path('check/', check_ans, name='check_ans'),
    path('', include((
        'url_shortner.urls', 'url_shortner'),
        namespace='url_shortner')),
    path('__debug__/', include('debug_toolbar.urls')),
]
