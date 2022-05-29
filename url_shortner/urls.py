from django.urls import path
from .views import redirect_url

urlpatterns = [
    path('<str:pk>', redirect_url, name='redirect_url')
]
