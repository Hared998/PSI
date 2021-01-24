from django.contrib import admin
from .models import Klient,Przystanek,Trasa,Kurs,KupioneBilety
# Register your models here.
admin.site.register(Klient)
admin.site.register(Przystanek)
admin.site.register(Trasa)
admin.site.register(Kurs)
admin.site.register(KupioneBilety)