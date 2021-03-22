from django.shortcuts import render, HttpResponse


def index(response):
    return render(response, 'mainapp/index.html', context={})


def products(response):
    return render(response, 'mainapp/products.html', context={})


def accounts(response):
    return render(response, 'mainapp/accounts.html', context={})

