from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, UserLoginForm, CustomUserCreationForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    if user.is_staff:  # Проверка на администратора
        return render(request, 'admin_profile.html', {'user': user})
    else:
        return render(request, 'profile.html', {'user': user})

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomUserCreationForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def manage_balance(request):
    return render(request, 'manage_balance.html')

@login_required
def deposit(request):
    return render(request, 'deposit.html')

@login_required
def withdraw(request):
    return render(request, 'withdraw.html')

@login_required
def transaction_history(request):
    return render(request, 'transaction_history.html')

@login_required
def create_game(request):
    # Представление для создания игр администратором
    if not request.user.is_staff:
        return redirect('profile')
    # Логика создания игры здесь
    return render(request, 'create_game.html')

@login_required
def monitor_games(request):
    # Представление для мониторинга игр администратором
    if not request.user.is_staff:
        return redirect('profile')
    # Логика мониторинга игр здесь
    return render(request, 'monitor_games.html')
