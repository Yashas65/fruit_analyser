from django.shortcuts import render


def index(request):

    context = {} # to frontend

    return render(request , 'page/index.html',context)
