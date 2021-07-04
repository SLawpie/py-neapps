from django.conf import settings
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from accounts.models import LoginAttempts

from device_detector import SoftwareDetector

context = {
        'app_name': settings.APP_NAME,
        'language_code': settings.LANGUAGE_CODE
    }

def start(request):
    return render(request, 'start/start.html', context)

@login_required(login_url='signin')
@csrf_protect
def home(request):
    # if request.user.AnonymousUser.is_authenticated:
    #     return redirect('signin')

    logins = LoginAttempts.objects.order_by("-created_at")[:10]
    logins_list = []
    for login in logins:
        device = SoftwareDetector(login.user_agent).parse()
        logins_list.append({
            'ip': login.ip,
            'user_name': login.user_name,
            'created_at': login.created_at,
            'browser': device.client_name() + " " + device.client_version(),
            'os': device.os_name() + " " + device.os_version(),
            'success': login.success
        })
    context['logins_list'] = logins_list
    return render(request, 'neapps/home.html', context)
