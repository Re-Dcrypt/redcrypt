from django.shortcuts import redirect
from url_shortner.models import UrlShortner


# Create your views here.


def redirect_url(request, pk):
    url_details = UrlShortner.objects.get(short_url=pk)
    url_details.click_counts += 1
    url_details.save()
    return redirect(url_details.full_url)
