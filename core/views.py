from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def cadastro(request):
    vnome = request.POST.get("name")
    vemail = request.POST.get("email")
    vsenha = request.POST.get("password")
    Pessoa.objects.create(nome=vnome, email=vemail, senha=vsenha)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa": pessoa})

def atualizar(request, id):
    vnome = request.POST.get("name")
    vemail = request.POST.get("email")
    vsenha = request.POST.get("password")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome =  vnome
    pessoa.email = vemail
    pessoa.senha = vsenha
    pessoa.save()
    return redirect(home)

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        print("Name:", name)
        print("Senha:", password)
        print(user)
        if user:
            auth_login(request, user)
            return render(request, 'login.html')
        else:
            messages.error(request, 'Credenciais inválidas')
    return render(request, 'login.html')
