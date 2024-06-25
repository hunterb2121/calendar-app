from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('events/', views.events, name='events'),
    path('events/<int:id>/', views.event_details, name='event_details'),
    path('share-calendar/', views.share_calendar, name='share_calendar'),
    path('shared-calendars/', views.shared_calendars, name='shared_calendars'),
    path('alerts/', views.alerts, name='alerts'),
]