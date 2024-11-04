from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('quotes/', views.quote, name='quote'),
    path('auhtor/', views.author, name='author'),
    path('tag/<str:tag>/', views.quotes_by_tag, name='quotes_by_tag'),
]