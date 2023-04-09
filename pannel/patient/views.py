# In signup_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    user = request.user
    context = {'user': user}
    return render(request, 'dashboard.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.profile_picture = form.cleaned_data.get('profile_picture')
            user.profile.address_line1 = form.cleaned_data.get('address_line1')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.state = form.cleaned_data.get('state')
            user.profile.pincode = form.cleaned_data.get('pincode')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def dashboard(request):
    user = request.user
    context = {'user': user}
    return render(request, 'dashboard.html', context)