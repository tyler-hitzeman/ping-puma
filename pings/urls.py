from django.urls import path

from . import views


urlpatterns = [
    # /pings/
    path('', views.index, name='index'),

    # /pings/add-ping/
    path('add-ping/', views.add_ping, name='add-ping'),

    # /pings/templates/
    path('templates/', views.templates, name='templates'),

    # /pings/history/
    path('history/', views.history, name='history'),

    # /pings/analytics/
    path('analytics/', views.analytics, name='analytics'),

]
