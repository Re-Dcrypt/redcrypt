"CustomMiddleware for IP Logging to user profile"
from ipware import get_client_ip
from accounts.models import Profile, IPs


class CustomMiddleware:
    "CustomMiddleware for ip logging"

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            client_ip, is_routable = get_client_ip(request)
            if request.user not in Profile.objects.all():
                user = Profile.objects.get_or_create(user=request.user)
            user = Profile.objects.get(user=request.user)
            if client_ip not in user.ip_address:
                user.ip_address.append(client_ip)
                user.ip_address_count += 1
                user.save()
            if client_ip not in IPs.objects.all():
                IPs.objects.get_or_create(ip_address=client_ip)
            ip_object = IPs.objects.get(ip_address=client_ip)
            if request.user not in ip_object.users_from_ip.all():
                ip_object.users_from_ip.add(request.user)
                ip_object.count += 1
            ip_object.save()
        return response
