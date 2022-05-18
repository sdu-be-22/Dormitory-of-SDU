from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book', views.book, name='book'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('logout', views.logout_user, name='logout'),
    path('profile', views.profile, name='profile'),
    path('booking_list/', views.booking_list, name='booking_list'),
    path('account_settings', views.account_settings, name='account_settings'),
    path('add_room', views.add_room, name='add_room'),
    path('room_list', views.room_list, name='room_list'),
]


