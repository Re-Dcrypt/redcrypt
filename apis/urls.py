from django.urls import path
from .views import get_profile

urlpatterns = [
    path('profile/<int:discord_id>', get_profile)
]
