from django.shortcuts import redirect, render
from url_shortner.models import UrlShortner


# Create your views here.


def redirect_url(request, slug):
    if len(UrlShortner.objects.filter(short_url=slug)) == 1:
        url_details = UrlShortner.objects.get(short_url=slug)
        if url_details.active:
            if request.user.is_authenticated and request.user not in url_details.visited_by.all():
                url_details.visited_by.add(request.user)
            url_details.click_counts += 1
            url_details.save()
            if url_details.is_content:
                return render(
                    request,
                    'shortner.html',
                    {'content': url_details.content,
                    'urlname': slug})
            return redirect(url_details.full_url)
        else:
            return redirect(f'{slug}/')
    return redirect(f'{slug}/')
