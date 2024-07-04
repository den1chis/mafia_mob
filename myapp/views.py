from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, UserLoginForm, CustomUserCreationForm, PasswordResetRequestForm, PhotoUploadForm, GameCreationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

import random
import string

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


def generate_random_password(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                new_password = generate_random_password()
                user.password = make_password(new_password)
                user.save()
                send_mail(
                    'Password Reset Request',
                    f'Your new password is: {new_password}',
                    'your-email@mail.ru',
                    [email],
                    fail_silently=False,
                )
                return redirect('password_reset_done')
            except User.DoesNotExist:
                form.add_error('email', 'Email address not found')
    else:
        form = PasswordResetRequestForm()
    return render(request, 'registration/password_reset_form.html', {'form': form})


def get_exif_data(image):
    exif_data = {}
    try:
        info = image._getexif()
        if info:
            for tag, value in info.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == "GPSInfo":
                    gps_data = {}
                    for gps_tag in value:
                        sub_tag = GPSTAGS.get(gps_tag, gps_tag)
                        gps_data[sub_tag] = value[gps_tag]
                    exif_data[tag_name] = gps_data
                else:
                    exif_data[tag_name] = value
    except AttributeError:
        pass
    return exif_data

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image_instance = Image.open(image)
            exif_data = get_exif_data(image_instance)
            gps_info = exif_data.get('GPSInfo')
            if gps_info:
                latitude = gps_info.get('GPSLatitude')
                longitude = gps_info.get('GPSLongitude')
                # Обработка данных GPS здесь
            # Сохранение изображения и данных здесь
            return redirect('profile')
    else:
        form = PhotoUploadForm()
    return render(request, 'upload_photo.html', {'form': form})

@login_required
def create_game(request):
    if request.method == 'POST':
        form = GameCreationForm(request.POST)
        if form.is_valid():
            # Сохранение данных игры и генерация ссылки
            game_link = "http://example.com/game/12345"  # Пример ссылки на игру
            return render(request, 'game_created.html', {'game_link': game_link})
    else:
        form = GameCreationForm()
    return render(request, 'create_game.html', {'form': form})