from django.urls import path
from .views import get_profile, verify_discord_id

urlpatterns = [
    path('profile/<int:discord_id>', get_profile),
    path('verify_discord_id/<int:discord_id>', verify_discord_id)
]
