from extra_settings.models import Setting
from django.shortcuts import redirect, render
from sentry_sdk import capture_exception


def hunt_status(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_staff:
            return function(request, *args, **kwargs)
        try:
            status = Setting.get('HUNT_STATUS', default="not started")
            if status == 'active':
                return function(request, *args, **kwargs)
            elif status == 'not started':
                t = Setting.get('HUNT_START_TIME')
                d = t.strftime("%m/%d/%Y %H:%M:%S")
                return render(request, 'not_active.html', {
                    'title': 'Starting soon',
                    'heading': 'The Hunt will be starting soon',
                    'time': d
                })
            elif status == 'paused':
                t = Setting.get('HUNT_RESUME_TIME')
                d = t.strftime("%m/%d/%Y %H:%M:%S")
                return render(request, 'not_active.html', {
                    'title': 'Hunt Paused',
                    'heading': 'Hunt has been paused',
                    'subheading': """Sorry for the inconvenience.
                    We will be back soon.""",
                    'time': d,

                })
            elif status == 'ended':
                return render(request, 'ended.html')
        except Exception as e:
            capture_exception(e)
            return redirect('index')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def not_banned(function):
    def wrap(request, *args, **kwargs):
        try:
            if request.user.profile.is_banned:
                return render(request, 'banned.html', {
                    'reason': request.user.profile.banned_reason})
            else:
                return function(request, *args, **kwargs)

        except Exception as e:
            capture_exception(e)
            return redirect('index')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
