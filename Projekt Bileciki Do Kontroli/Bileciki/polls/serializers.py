from rest_framework import serializers
from .models import Stop, Track, Client, Ticket
from django.contrib.auth.models import User

class StopSerializer(serializers.HyperlinkedModelSerializer):

    tracks = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='track-detail')

    class Meta:
        model = Stop
        fields = ['pk', 'url', 'name', 'tracks']


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    stop = serializers.SlugRelatedField(queryset=Stop.objects.all(), slug_field='name')
    tickets = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='ticket-detail')

    class Meta:
        model = Track
        fields = ['pk', 'url', 'track_name', 'start_date', 'stop', 'tickets']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    tickets = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='ticket-detail')

    class Meta:
        model = Client
        fields = ['url', 'pk', 'name', 'surname', 'birth', 'address', 'tickets']


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    buyer = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='surname')
    track = serializers.SlugRelatedField(queryset=Track.objects.all(), slug_field='track_name')

    class Meta:
        model = Ticket
        fields = ['pk', 'url', 'owner', 'buyer', 'track', 'price']
class UserBiletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ['url','track']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    tickets = TicketSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ['url','pk','username','tickets']
