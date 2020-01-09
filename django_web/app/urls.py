"""
单元下新创建一个子路由
然后在django_web/urls配置只路由的分发

"""
from django.conf.urls import url
from app import views

urlpatterns = [
    url('a/', views.a)
]