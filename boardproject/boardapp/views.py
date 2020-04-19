from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
        usernamex = request.POST['username']
        passwordx = request.POST['username']
        try:
            User.objects.get(username=usernamex)
            return render(request, 'signup.html', {'error':'this user already exists'})
        except:
            user = User.objects.create_user(usernamex, '', passwordx)
            return render(request, 'signup.html', {'some':200})

        return render(request, 'signup.html', {'some':200})
    return render(request, 'signup.html', {'some':200})


def loginfunc(request):
    if request.method == 'POST':
        usernamex = request.POST['username']
        passwordx = request.POST['username']
        user = authenticate(request, username=usernamex,password=passwordx)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')

    return render(request, 'login.html')

@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})


def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good += 1
    post.save()
    return redirect('list')


def readfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('list')
    else:
        post.read += 1
        post.readtext = post.readtext + ' ' + post2
        post.save()
    return redirect('list')

class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title','content','author','images')
    success_url = reverse_lazy('list')
