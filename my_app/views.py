from django.shortcuts import render, HttpResponse


def page1(request):
    return HttpResponse('Это страница 1')


def page2(request):
    return HttpResponse('Это страница 2')