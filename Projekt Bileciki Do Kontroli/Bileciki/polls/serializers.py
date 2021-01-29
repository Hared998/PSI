from rest_framework import serializers
from .models import Stop, Track, Client, Ticket


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
    buyer = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='surname')
    track = serializers.SlugRelatedField(queryset=Track.objects.all(), slug_field='track_name')

    class Meta:
        model = Ticket
        fields = ['pk', 'url', 'buyer', 'track', 'price']