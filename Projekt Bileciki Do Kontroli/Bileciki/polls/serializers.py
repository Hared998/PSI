from rest_framework import serializers
from .models import Klient, Przystanek, Kurs, KupioneBilety, Trasa


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ['Imie','Nazwisko','Wiek','NrTel','Email','RodzajUlgi']


class PrzystanekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Przystanek
        fields = ['Nazwa']


class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurs
        fields = ['Przewoznik','ilosc_miejsc','Cena']


class KupioneBilety(serializers.ModelSerializer):
    class Meta:
        model = KupioneBilety
        fields = ['idBilet','idKlient','idKurs']


class TrasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trasa
        fields = ['czas','idPrzystanek']