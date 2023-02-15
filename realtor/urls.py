
from django.urls import path
from .views import *

urlpatterns = [
    path('',AgentListView.as_view(),name='contact'),
    ]
