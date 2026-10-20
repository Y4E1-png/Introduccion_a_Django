import os

from django import get_version
from django.conf import settings
from django.shortcuts import render
from pages.clases import Auto
from pages.clases import Refaccion

def home(request):
    coche = Auto("Peugeot", "508", "2018")
    refaccion = Refaccion("Amortiguador")

    context = {
        "mi_auto": coche,
        "mi_refaccion": refaccion,
        "debug": settings.DEBUG,
        "django_ver": get_version(),
        "python_ver": os.environ["PYTHON_VERSION"],
    }

    return render(request, "pages/home.html", context)
