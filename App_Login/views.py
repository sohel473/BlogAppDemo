from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Login.forms import SignUpForm, UserProfileChange, ProfilePic

# Create your views here.


def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == "POST":
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    dict = {
        'form': form,
        'registered': registered
    }

    return render(request, 'App_Login/sign_up.html', context=dict)


def login_page(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return (HttpResponseRedirect(reverse('index')))

    dict = {
        'form': form
    }
    return render(request, "App_login/login.html", context=dict)


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    dict = {

    }
    return render(request, "App_login/profile.html", context=dict)


@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == "POST":
        form = UserProfileChange(data=request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
            return HttpResponseRedirect(reverse('App_Login:profile'))
    dict = {
        'form': form
    }
    return render(request, "App_Login/change_profile.html", context=dict)


@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(user=current_user)
    if request.method == "POST":
        form = PasswordChangeForm(user=current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    dict = {
        'form': form,
        'changed': changed
    }
    return render(request, "App_Login/change_pass.html", context=dict)


@login_required
def add_pro_pic(request):
    form = ProfilePic()
    if request.method == "POST":
        form = ProfilePic(data=request.POST, files=request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))

    dict = {
        'form': form
    }
    return render(request, 'App_Login/pro_pic_add.html', context=dict)


@login_required
def change_pro_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == "POST":
        form = ProfilePic(data=request.POST, files=request.FILES,
                          instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    dict = {
        'form': form
    }
    return render(request, 'App_Login/pro_pic_add.html', context=dict)
