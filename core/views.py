from django.shortcuts import render, redirect
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
