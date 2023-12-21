from django.urls import path

from . import views

app_name = 'event'
urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('events/<int:id>/', views.event_detail, name='event_detail'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/update/<int:id>/', views.event_update, name='event_update'),
]
