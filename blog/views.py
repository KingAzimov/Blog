from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import *
from .models import *

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(username=request.POST.get('l'),
                            password=request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/blog/')

class BlogView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data={
                'maqola':Maqola.objects.filter(muallif__user=request.user)
            }
            return render(request, 'blog.html', data)
        else:
            return redirect('/')
    def post(self, request):
        if request.user.is_authenticated:
            Maqola.objects.create(
                sarlavha=request.POST.get("s"),
                sana=request.POST.get("sana"),
                mavzu=request.POST.get("m"),
                matn=request.POST.get("matn"),
                muallif=Muallif.objects.get(ism__contains="i")
            )
            return redirect('/blog/')
        else:
            return redirect('/')

class RegisterView(View):
    def get(self, request):
            return render(request, 'register.html')

    def post(self, request):
            User.objects.create_user(
                username=request.POST.get('l'),
                password=request.POST.get('p')
                )
            return redirect('/')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class MaqolaView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            data={
                'maqola': Maqola.objects.get(id=pk)
            }
            return render(request, 'maqola.html', data)
        else:
            return redirect('/')