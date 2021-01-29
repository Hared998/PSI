from django.db import models


class Stop(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Track(models.Model):
    track_name = models.CharField(max_length=50)
    start_date = models.DateField()
    stop = models.ForeignKey(Stop, related_name='tracks', on_delete=models.CASCADE)

    def __str__(self):
        return self.track_name


class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth = models.DateField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + self.surname


class Ticket(models.Model):
    buyer = models.ForeignKey(Client, related_name='tickets', on_delete=models.CASCADE)
    track = models.ForeignKey(Track, related_name='tickets', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
