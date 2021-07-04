from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import logout

context = {
        'app_name': settings.APP_NAME,
        'language_code': settings.LANGUAGE_CODE
    }

def csrf_failure(request, reason=""):
    logout(request)
    return render(request, 'neapps/403.html', context)