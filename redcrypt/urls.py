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
from hunt.views import index
from accounts import views as accounts_views


urlpatterns = [
    path('', index, name='index'),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('honeypot/', admin.site.urls),
    path('api/', include(('apis.urls', 'apis'), namespace='api')),
    path('', include((
        'url_shortner.urls', 'url_shortner'),
        namespace='url_shortner')),
    path(
        'accounts/social/connections/',
        accounts_views.connect, name='connect'),
    path('accounts/', include('allauth.urls')),

    path('profile/', accounts_views.profile, name='profile'),

]
