from django.shortcuts import render, redirect
from .forms import MiUserCreationForm, MiUserLoginForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages





def authenticated(request):
    data= {
        'form':MiUserCreationForm
    }
    if request.method == 'POST':
        Miform = MiUserCreationForm(data=request.POST)
        if Miform.is_valid():
            Miform.save()
            user=authenticate(username=Miform.cleaned_data['username'],password=Miform.cleaned_data['password1'])
            login(request, user)

            return redirect('inicio')  # Reemplaza 'página_de_inicio' con el nombre de la vista de tu página principal
    else:
        Miform= MiUserCreationForm()
    return render(request, 'authenticated/registro.html', data)

def cerra_sesion(request):
    logout(request)
    return redirect('inicio')

def logear(request):
    if request.method == 'POST':
        form = MiUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']  # Corrección: Elimina el espacio entre 'password' y los corchetes
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio') # Reemplaza 'inicio' con el nombre de la vista de tu página principal
            else:
                messages.error(request, "Usuario No Valido")
        else:
            messages.error(request, "Información incorrecta")

    form = MiUserLoginForm()
    return render(request, 'authenticated/login.html', {'form': form})

