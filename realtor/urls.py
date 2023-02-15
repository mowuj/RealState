
from django.urls import path
from .views import *

urlpatterns = [
    path('',AgentListView.as_view(),name='agentlist'),
    path('<pk>/', AgentDetailView.as_view(), name='agent-detail'),
    path('topseller', TopSellerListView.as_view(), name='top-seller'),
    ]
