from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Klient, Przystanek, Kurs, KupioneBilety, Trasa
from .serializers import KlientSerializer, PrzystanekSerializer, KursSerializer, KupioneBiletySerializer,TrasaSerializer


def index(request):
    return HttpResponse("hello, world")
