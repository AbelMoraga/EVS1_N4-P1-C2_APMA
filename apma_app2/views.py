from django.shortcuts import render
from django.http import HttpResponse


def vistaTres(request):
    html = """
    <h1 style="color:blue">esta es la rama 2</h1>
    """
    return HttpResponse(html)


def vistaCuatro(request):
    html = """
    <h1 style="color:red">esta es la segunda vista de la rama 2</h1>
    """
    return HttpResponse(html)



# Create your views here.
