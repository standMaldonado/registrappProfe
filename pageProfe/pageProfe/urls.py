from django.contrib import admin
from django.urls import path
from profesores import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('asignaturas/', views.asignaturas, name='asignaturas'),
    path('inicio-docente/', views.inicio_docente, name='inicio-docente'),
    path('', views.login_view, name='login'),
    path('olvide-contrasena/', views.olvide_contrasena, name='olvide-contrasena'),
    path('registro/',views.registro, name='registro'),
]
