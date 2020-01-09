from django.shortcuts import render
from django.http import HttpResponse


# def index(req):
#     return render(req, 'index.html')


def a(req):
    return HttpResponse("A - 是app下子路由才能进入的页面")
