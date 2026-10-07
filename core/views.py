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
        Race("Circuit lemans F1", 200, "Le Mans", "https://thumb.wikimedia.org/wikipedia/commons/thumb/6/69/Bugatti_Circuit.svg/1280px-Bugatti_Circuit.svg.png?utm_source=fr.wikipedia.org&utm_campaign=index&utm_content=thumbnail"),
        Race("Circuit de L'Université F4", 150, "Lyon", "https://image.over-blog.com/DRBlqQZ-clIz3A7dp36pp1dMEsg=/filters:no_upscale()/image%2F0666730%2F20220127%2Fob_dcae50_capture-d-e-cran-2022-01-27-a-14.png"),
        Race("Circuit LeChatDuPain F3", 500, "Paris", "https://static.wixstatic.com/media/55988d_f16fe29722aa43bc88c84d34155b9004~mv2.png/v1/fill/w_568,h_378,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/55988d_f16fe29722aa43bc88c84d34155b9004~mv2.png"),
    ]
    return render(request, "core/racing.html", {"courses": courses})