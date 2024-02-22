from django.urls import path
from .views import index,contact,product
from django.conf.urls import handler404,handler500
from core import views
urlpatterns=[
    path('',index, name='index'),
    path('contact/',contact, name='contact'),
    path('product/<int:pk>',product,name='product'),
]
handler404=views.error404
handler500=views.error500