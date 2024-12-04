from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView

from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from .forms import ProfileForm, RegisterForm
# Create your views here.

def register_user(request):
    if request.user.is_authenticated:
        return redirect('quotes:root')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:root')
        else:
            return render(request, 'users/register.html', context={'form': form})
        
    return render(request, 'users/register.html', context={'form': RegisterForm()})
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password1']
    #         user = authenticate(username=username, password=password)

    #         if user is not None:
    #             login(request,user)
    #             messages.success(request, f"Account created for {username}!")
    #             return redirect('users:login')
    #         else:
    #             messages.error(request,"user authentication failed")
    #     else:
    #         messages.error(request, "There was a problem with your registration")
    # else:
    #     form=UserCreationForm()
    # return render(request, 'users/register.html', {
    #     'form': form,
    # })

@csrf_exempt
def login_user(request):
    if request.user.is_authenticated:
        return redirect('quotes:root')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('quotes:root')
        else:
            messages.success(request, ("There was an error loggin in, try again") )
            return redirect('users:login')
    else:
        return render(request, 'users/login.html', {} )
    
@login_required
def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out!!") )
    return redirect('quotes:root')

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users:profile')

    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'profile_form': profile_form})

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_form.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = "An message with password reset has been sent to %(email)s."
    subject_template_name = 'users/password_reset_subject.txt'