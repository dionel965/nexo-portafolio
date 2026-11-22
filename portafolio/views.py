# Create your views here.
from django.shortcuts import render


def inicio(request):
    contexto = {"page_title": "Nexo — Portafolio", "active_page": "inicio"}
    return render(request, "portafolio/inicio.html", contexto)


def sobre_mi(request):
    contexto = {"page_title": "Sobre mí — Nexo", "active_page": "sobre_mi"}
    return render(request, "portafolio/sobre_mi.html", contexto)


def habilidades(request):
    contexto = {"page_title": "Habilidades — Nexo", "active_page": "habilidades"}
    return render(request, "portafolio/habilidades.html", contexto)


def proyectos(request):
    contexto = {"page_title": "Proyectos — Nexo", "active_page": "proyectos"}
    return render(request, "portafolio/proyectos.html", contexto)


def contacto(request):
    contexto = {"page_title": "Contacto — Nexo", "active_page": "contacto"}
    return render(request, "portafolio/contacto.html", contexto)