from django.shortcuts import render, HttpResponse


def index(response):
    return HttpResponse('Hello')