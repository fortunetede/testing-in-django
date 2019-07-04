from django.urls import path
from links import views


urlpatterns = [
    path('links/', views.index ),
    path('tag/<tag>/', views.index ),
]
