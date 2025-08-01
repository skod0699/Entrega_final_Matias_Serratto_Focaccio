from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.views import LoginView, LogoutView
from accounts.models import Profile

def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Cuenta creada con éxito.')
            login(request, user)
            return redirect('novedades:home')  # Cambié 'home' por la url correcta
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'

@login_required
def profile_view(request):
    user = request.user

    # Asegurarse que el perfil exista o crearlo si no
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            print("Formularios válidos, guardando...")
            u_form.save()
            p_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado.')
            return redirect('accounts:profile')
        else:
            print("Errores en formulario usuario:", u_form.errors)
            print("Errores en formulario perfil:", p_form.errors)
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/profile.html', context)
