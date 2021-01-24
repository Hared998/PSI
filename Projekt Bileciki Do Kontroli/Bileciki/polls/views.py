from django.shortcuts import render
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Klient, Przystanek, Kurs, KupioneBilety, Trasa
from .serializers import KlientSerializer, PrzystanekSerializer, KursSerializer, KupioneBiletySerializer,TrasaSerializer
from django.contrib.auth.models import User


class KlientAPIView(APIView):
    serializer_class = KlientSerializer

    def get_querryset(self):
        klienci = Klient.objects.all()
        return klienci

    def get(self,request, *args, **kwargs):
        klienci = self.get_querryset()
        serializer = KlientSerializer(klienci, many=True)

        return Response(serializer.data)



class ListaKursow(generics.ListCreateAPIView):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
    name = 'kurs-list'
    filter_fields = ['Przewoznik','ilosc_miejsc','Cena']
    search_fields = ['Przewoznik', 'Cena']
    ordering_fields = ['Przewoznik', 'Cena']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TrasaList(generics.ListCreateAPIView):
    queryset = Trasa.objects.all()
    serializer_class = TrasaSerializer
    filter_class = 'TrasaFilter'
    name = 'Trasa-list'
    ordering_fields = ['IdKurs', 'czas']

