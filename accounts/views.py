from device_detector.parser.settings import AVAILABLE_ENGINES_LOWER_CASE
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from accounts.models import LoginAttempts

# from .forms import UserCreationForm

context = {
        'app_name': settings.APP_NAME,
        'language_code': settings.LANGUAGE_CODE,
        'username': '',
        'messages': ''
    }

def signup(request):
    # form = UserCreationForm()
    # context.update({'form': form})
    return render(request, 'accounts/signup.html', context)


def signout(request):
    logout(request)
    # return render(request, 'accounts/signin.html', context)
    return redirect('start')

def signin(request):
    if request.user.is_authenticated:
        #return render(request, 'start/home.html', context)
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            ua = request.META.get('HTTP_USER_AGENT')
            ip = get_client_ip(request)
            if user is not None:
                login(request, user)
                success = True
                LoginAttempts.objects.create(
                    ip=ip,
                    user_name=username,
                    user_agent=ua,
                    success = success
                )
                return redirect('home')
            else:
                # messages.info(request, 'Niepoprawny użytkownik lub hasło')
                # context.update({'messages': 'Niepoprawny użytkownik lub hasło'})
                context['messages'] = 'Niepoprawny użytkownik lub hasło'
                success = False
                LoginAttempts.objects.create(
                    ip=ip,
                    user_name=username,
                    user_agent=ua,
                    success = success
                )
        else:
            context['messages'] = ""

        #return redirect('signin')
        return render(request, 'accounts/signin.html', context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # print "returning FORWARDED_FOR"
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        # print "returning REAL_IP"
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        # print "returning REMOTE_ADDR"
        ip = request.META.get('REMOTE_ADDR')
    return ip
