from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post
# from django.http import HttpResponse
# Create your views here.

users = User.objects.all()
posts = Post.objects.all()
operations = [
  {
    "codigo": 1,
    "operacao": "PLANTIO CANA",
    "frentes": ["Frente 4", "frente 5", "frente 6"]
  },
  {
    "codigo": 2,
    "operacao": "COLHEITA CANA CRUA",
    "frentes": ["Frente 4", "frente 5", "frente 6"]
  },
  {
    "codigo": 3,
    "operacao": "PLANTIO SOJA",
    "frentes": ["Frente 4", "frente 5", "frente 6"]
  },
  {
    "codigo": 4,
    "operacao": "COLHEITA SOJA",
    "frentes": ["Frente 4", "frente 5", "frente 6"]
  },
  {
    "codigo": 7,
    "operacao": "SEM LOCACAO",
    "frentes": ["Frente 4", "frente 5", "frente 6"]
  },
  {
    "codigo": 8,
    "operacao": "APLICACAO",
    "frentes": ["Frente 4", "frente 5", "frente 6"]
  },
  {
    "codigo": 9,
    "operacao": "CTT",
    "frentes": ["Frente 4", "frente 5", "frente 6"]
  },
  {
    "codigo": 10,
    "operacao": "TRATOS CULTURAIS",
    "frentes": ["Frente 4", "frente 5", "frente 6"]
  },
  {
    "codigo": 11,
    "operacao": "PLANTIO IRRIGADO",
    "frentes": ["Frente 4", "frente 5", "frente 6"]
  },
  {
    "codigo": 12,
    "operacao": "PREPARO",
    "frentes": ["Frente 4", "frente 5", "frente 6"]
  },
  {
    "codigo": 13,
    "operacao": "FERTIRRIGACAO",
    "frentes": ["Frente 4", "frente 5", "frente 6"]
  },
  {
    "codigo": 14,
    "operacao": "HERBICIDA",
    "frentes": ["Frente 4", "frente 5", "frente 6"]
  },
  {
    "codigo": 15,
    "operacao": "IRRIGACAO SALVAMENTO",
    "frentes": ["Frente 4", "frente 5", "frente 6"]
  },
  {
    "codigo": 16,
    "operacao": "VINHACA LOCALIZADA",
    "frentes": ["Frente 4", "frente 5", "frente 6"]
  }
]


def home(request):
    context = {
        'posts': posts,
        'users': users,
    }
    return render(request, 'blog/operation_front.html', context)

def operation(request):
    context = {
        'operations': operations,
        'users': users,
    }
    return render(request, 'blog/operations.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
