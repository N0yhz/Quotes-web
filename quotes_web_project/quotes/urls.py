from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('tag/', views.tag_list, name='tag_list'),
    path('tag/<int:tag_id>/', views.quotes_by_tag, name='quotes_by_tag'),
]