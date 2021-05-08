from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# from .forms import UserCreationForm

context = {
        'app_name': settings.APP_NAME,
        'language_code': settings.LANGUAGE_CODE
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

            context.update({'user': username})
            if user is not None:
                login(request, user)
                return render(request, 'neapps/home.html', context)
            else:
                messages.info(request, 'Niepoprawny użytkownik lub hasło')

        return render(request, 'accounts/signin.html', context)