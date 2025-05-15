from django.urls import path
from . import views

app_name = 'orm_abc_app'

urlpatterns = [
    path('',        views.abc_form,   name='abc_form'),
    path('result/', views.abc_result, name='abc_result'),
    path('table/',  views.table,      name='table'),
]
