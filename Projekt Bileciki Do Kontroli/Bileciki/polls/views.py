from django.shortcuts import render
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Klient, Przystanek, Kurs, KupioneBilety, Trasa
from .serializers import KlientSerializer, PrzystanekSerializer, KursSerializer, KupioneBiletySerializer,TrasaSerializer
from django.contrib.auth.models import User


class KlientLista(generics.ListCreateAPIView):
    permission_classes = permissions.IsAdminUser,
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer


class PrzystanekLista(generics.ListCreateAPIView):

    permission_classes = permissions.IsAdminUser,
    queryset = Przystanek.objects.all()
    serializer_class = PrzystanekSerializer


class TrasaLista(generics.ListCreateAPIView):
    permission_classes = permissions.IsAdminUser,
    queryset = Trasa.objects.all()
    serializer_class = TrasaSerializer
#coś nowego

class KursLista(generics.ListCreateAPIView):
    permission_classes = permissions.IsAdminUser,
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer


class BiletyLista(generics.ListCreateAPIView):
    permission_classes = permissions.IsAuthenticatedOrReadOnly,
    queryset = KupioneBilety.objects.all()
    serializer_class = KupioneBiletySerializer