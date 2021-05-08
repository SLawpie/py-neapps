from django.conf import settings
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

context = {
        'app_name': settings.APP_NAME,
        'language_code': settings.LANGUAGE_CODE
    }

def start(request):
    return render(request, 'start/start.html', context)

@login_required(login_url='signin')
def home(request):
    # if request.user.AnonymousUser.is_authenticated:
    #     return redirect('signin')
    return render(request, 'neapps/home.html', context)