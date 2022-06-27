from django.urls import re_path as url

from pwa.views import manifest, service_worker, offline

# Serve up serviceworker.js and manifest.json at the root
urlpatterns = [
    url('serviceworker.js', service_worker, name='serviceworker'),
    url('manifest.json', manifest, name='manifest'),
    url('offline/', offline, name='offline')
]
