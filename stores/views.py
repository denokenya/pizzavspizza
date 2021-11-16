from django.shortcuts import render
from rest_framework import generics
from .serializers import (
    PizzeriaListSerializer,
    PizzeriaDetailSerializer,
)

from .models import Pizzeria


class PizzeriaListAPIView(generics.ListAPIView):
    """ListAPIView for all pizzeria """
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaListSerializer


class PizzeriaRetrieveAPIView(generics.RetrieveAPIView):
    """DetailAPIView for all pizzeria"""
    lookup_field = "id"
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer


class PizzeriaCreateAPIView(generics.CreateAPIView):
    """CreateAPI for pizzeria"""
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer


class PizzeriaRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """RetrieveUPdateAPI for the pizzeria"""

    lookup_field = "id"
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer


class PizzeriaDestroyAPIView(generics.DestroyAPIView):
    """DestroyAPIView for the pizzeria"""
    lookup_field = "id"
    queryset = Pizzeria.objects.all()
