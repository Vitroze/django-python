from django.shortcuts import render
from .models.race import Race

def index(request):
    nom = request.GET.get("nom", "").strip() or "le monde"
    cours = ["Python", "Django", "HTML / CSS"]
    return render(request, "core/index.html", {"nom": nom, "cours": cours})


def about(request):
    return render(request, "core/about.html")

def racingpage(request):
    courses = [
        Race("Circuit lemans F1", 200, "Le Mans", "lemans.jpg"),
        Race("Circuit de L'Université F4", 150, "Lyon", "universite.jpg"),
        Race("Circuit LeChatDuPain F3", 500, "Paris", "chatdupain.jpg"),
    ]
    return render(request, "core/racing.html", {"courses": courses})