from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeListAPIView.as_view(), name='home'),
    path('search/', Search.as_view(), name='search'),
    path('<slug>/', HomeDetailAPIView.as_view(), name='home-detail'),
    path('images/<pk>/', ImageView.as_view(), name='images'),
]
