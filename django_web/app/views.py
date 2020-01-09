from django.shortcuts import render
from django.http import HttpResponse



def index(req):
    return HttpResponse('Django index')

def a(req):
    return HttpResponse("A - 是app下子路由才能进入的页面")
