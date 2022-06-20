from django.urls import path
from .views import redirect_url

urlpatterns = [
    path('<str:slug>', redirect_url, name='redirect_url')
]
