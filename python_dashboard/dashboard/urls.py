from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.main_panel, name='main_panel'),
    path('<str:app_name>/', views.app_frame, name='app_frame'),
]
