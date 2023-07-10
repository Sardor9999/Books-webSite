from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def  main_page(request: HttpRequest):
    #Logika yoziladi bu joyga
    return HttpResponse("Hello Django")