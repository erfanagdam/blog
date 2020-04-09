from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        if request.POST.get('password') == request.POST.get('password-retype'):
            try:
                user = User.objects.get(username = request.POST.get('username'))
                return render(request, 'signup.html', {'error':'username error'})
            except User.DoesNotExist:
                user = User.objects.create_user(usernam = request.POST.get('username'), password = request.POST.get('password') )
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error':'password error'})
    else:
     return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username =request.POST.get('username'), password = request.POST.get('password'))
        if user is not None:
            auth.login(request, user)
            return redirect('comment')
        else :
            return render(request, 'comment.html', {'error':'user not found'})

#    else:
#        return render(request, 'login.html')




def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request, 'index.html')
