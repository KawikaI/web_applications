from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import StudentSignUpForm, TASignUpForm
from .models import CustomUser, TAInfo
from django.shortcuts import redirect


def home(request):
    return render(request, 'accounts/home.html')  # Create a simple homepage template

def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'student'
            user.save()
            login(request, user)
            return redirect('student_dashboard')
    else:
        form = StudentSignUpForm()
    return render(request, 'accounts/student_signup.html', {'form': form})

def ta_signup(request):
    if request.method == 'POST':
        form = TASignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'ta'
            user.save()
            # Save additional TA info
            TAInfo.objects.create(
                user=user,
                class_tutoring=form.cleaned_data.get('class_tutoring'),
                times_available=form.cleaned_data.get('times_available'),
                days_available=form.cleaned_data.get('days_available')
            )
            login(request, user)
            return redirect('ta_dashboard')  # Redirect after successful signup
    else:
        form = TASignUpForm()
    return render(request, 'accounts/ta_signup.html', {'form': form})

@login_required
def student_dashboard(request):
    tas = TAInfo.objects.all()
    return render(request, 'accounts/student_dashboard.html', {'tas': tas})

@login_required
def ta_dashboard(request):
    ta_info = TAInfo.objects.get(user=request.user)
    return render(request, 'accounts/ta_dashboard.html', {'ta_info': ta_info})


def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'student'
            user.save()
            login(request, user)
            return redirect('student_dashboard')  # Redirect to the dashboard after signup
    else:
        form = StudentSignUpForm()
    return render(request, 'accounts/student_signup.html', {'form': form})