from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.getroutes),
    path('rooms/', views.getrooms),
    path('rooms/<str:pk>/', views.getroom),
]
