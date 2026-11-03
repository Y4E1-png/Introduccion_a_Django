from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm


def registro(request):
  if request.method == "POST":
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "La cuenta se creó correctamente.")
      return redirect("register_form")
    messages.error(request, "No se pudo crear la cuenta. Revisa los errores del formulario.")
  else:
    form = UserForm()

  return render (request, "registro.html", {"form":form} ) 
