from django.shortcuts import render, redirect
from .loginform import LoginForm
from .models import Users


def index(request):
    return render(request, 'index.html')


def show_login(request):
    return render(request, 'login.html')


def login(request):
    error = ''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():

            if Users.objects.filter(username=form.clean_login_name()).exists():

                return redirect('home', userinfo=Users.objects.get(username=form.clean_login_name()).userinfo)
            else:
                error = 'error4'
        else:
            error = 'error5'

    form = LoginForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'login.html', context)


def home(request, userinfo):
    print(userinfo)
    context = {
        'userinfo': userinfo
    }
    return render(request, 'home.html',context)