from django.shortcuts import render


def index(request):
    nom = request.GET.get("nom", "").strip() or "le monde"
    cours = ["Python", "Django", "HTML / CSS"]
    return render(request, "core/index.html", {"nom": nom, "cours": cours})


def about(request):
    return render(request, "core/about.html")
