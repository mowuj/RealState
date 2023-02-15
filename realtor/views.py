# from django.shortcuts import render
# from rest_framework import permissions
# from .models import Agent
# from .serializers import *
# from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView
# # Create your views here.

# class AgentListView(ListAPIView):
#     permission_classes=(permissions.AlloyAny)
#     queryset=Agent.objects.all()
#     serializer=AgentSerializer
#     pagination_class=None

# class AgentDetailView(RetrieveAPIView):
#     queryset=Agent.objects.all()
#     serializer_class=AgentSerializer
