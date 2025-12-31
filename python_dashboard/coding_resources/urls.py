from django.urls import path
from . import views

app_name = 'coding_resources'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.topic_list, name='topic_list'),
    path('topic/<int:topic_id>/', views.snippet_list, name='snippet_list'),
]
