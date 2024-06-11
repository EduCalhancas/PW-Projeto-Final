from django.shortcuts import render, redirect
from django.contrib.auth import models, authenticate, login, logout


def registo_curso_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('login_curso')

    return render(request, 'autenticacao/registo_curso.html')


def login_curso_view(request):
    if request.method == "POST":

        # Verifica as credenciais
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            # Se as credenciais são válidas, faz login e redireciona
            login(request, user)
            return render(request, 'autenticacao/user_curso.html')
        else:
            # Se inválidas, reenvia para login com mensagem
            render(request, 'autenticacao/login_curso.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'autenticacao/login_curso.html')


def logout_curso_view(request):
    logout(request)
    return redirect('curso:index')