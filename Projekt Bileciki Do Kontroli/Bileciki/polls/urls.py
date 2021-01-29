from django.urls import path
from . import views
urlpatterns = [
    path('stops',views.StopList.as_view(), name=views.StopList.name),
    path('stops/<int:pk>',views.StopDetail.as_view(), name=views.StopDetail.name),
    path('tracks',views.TrackList.as_view(), name=views.TrackList.name),
    path('tracks<int:pk>',views.TrackDetail.as_view(), name=views.TrackDetail.name),
    path('clients',views.ClientList.as_view(), name=views.ClientList.name),
    path('clients<int:pk>',views.ClientDetail.as_view(), name=views.ClientDetail.name),
    path('tickets',views.TicketList.as_view(), name=views.TicketList.name),
    path('tickets<int:pk>',views.TrackDetail.as_view(), name=views.TrackDetail.name),
    path('',views.ApiRoot.as_view(), name=views.ApiRoot.name),
    ]
