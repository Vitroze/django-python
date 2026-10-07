from django.shortcuts import render


def index(request):
    nom = request.GET.get("nom", "").strip() or "le monde"
    cours = ["Python", "Django", "HTML / CSS"]
    return render(request, "core/index.html", {"nom": nom, "cours": cours})


def about(request):
    return render(request, "core/about.html")

def racingpage(request):
    courses = [
        "Circuit lemans F1 - 200KM",
        "Circuit de L'Univerwww F4 - 150KM",
        "Circuit LeChatDuPain F3 - 500KM",
    ]
    return render(request, "core/racing.html", {"courses": courses})