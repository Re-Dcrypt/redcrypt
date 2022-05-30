"CustomMiddleware for IP Logging to user profile"
from ipware import get_client_ip
from accounts.models import Profile


class CustomMiddleware:
    "CustomMiddleware for ip logging"

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            client_ip, is_routable = get_client_ip(request)
            print(client_ip)
            user = Profile.objects.get(user=request.user)
            if client_ip not in user.ip_address:
                user.ip_address.append(client_ip)
                user.save()
            print("Authenticated")

        return response
