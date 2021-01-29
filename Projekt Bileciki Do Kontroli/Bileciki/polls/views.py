from rest_framework import generics
from rest_framework import permissions
from django_filters import DateTimeFilter, FilterSet
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Stop, Track, Client, Ticket
from .serializers import StopSerializer, TrackSerializer, ClientSerializer, TicketSerializer


class StopList(generics.ListCreateAPIView):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    name = 'stop-list'


class StopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    name = 'stop-detail'


class TrackList(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    name = 'track-list'


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    name = 'track-detail'


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-list'


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'


class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    name = 'ticket-list'


class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    name = 'ticket-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request , *args, **kwargs):
        return Response({'stops': reverse(StopList.name, request=request),
                         'tracks': reverse(TrackList.name, request=request),
                         'clients': reverse(ClientList.name, request=request),
                         'tickets': reverse(TicketList.name, request=request)})