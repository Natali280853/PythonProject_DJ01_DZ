from django.shortcuts import render
from django.http import HttpResponse


def data_view(request):
    return HttpResponse("<h1>Содержимое страницы Data</h1><p>Это страница с данными.</p>")


def test_view(request):
    return HttpResponse("<h1>Содержимое страницы Test</h1><p>Это страница тестирования.</p>")
