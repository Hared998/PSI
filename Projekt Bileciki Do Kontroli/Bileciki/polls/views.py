from rest_framework import generics
from rest_framework import permissions
from django_filters import DateTimeFilter, FilterSet, NumberFilter, AllValuesFilter
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Stop, Track, Client, Ticket
from .serializers import StopSerializer, TrackSerializer, ClientSerializer, TicketSerializer, UserSerializer, UserBiletSerializer
from django.contrib.auth.models import User

class StopList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    name = 'stop-list'
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']


class StopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    name = 'stop-detail'


class TrackList(generics.ListCreateAPIView):

    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    name = 'track-list'
    filter_fields = ['track_name', 'start_date']
    search_fields = ['track_name']
    ordering_fields = ['start_date']


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    name = 'track-detail'

class ClientFilter(FilterSet):
    from_birthdate = DateTimeFilter(field_name='birth', lookup_expr='gte')
    to_birthdate = DateTimeFilter(field_name='birth', lookup_expr='lte')

    class Meta:
        model = Client
        fields = ['from_birthdate','to_birthdate']


class ClientList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_class = ClientFilter
    name = 'client-list'


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'

class TicketFilter(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')
    track_name = AllValuesFilter(field_name='track__track_name')

    class Meta:
        model = Ticket
        fields = ['min_price', 'max_price', 'track_name']


class TicketList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_class = TicketFilter
    name = 'ticket-list'

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    name = 'ticket-detail'

class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request , *args, **kwargs):
        return Response({'stops': reverse(StopList.name, request=request),
                         'users': reverse(UserList.name,request=request),
                         'tracks': reverse(TrackList.name, request=request),
                         'clients': reverse(ClientList.name, request=request),
                         'tickets': reverse(TicketList.name, request=request)})