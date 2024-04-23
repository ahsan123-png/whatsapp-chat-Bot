from django.urls import path
from .views import *

urlpatterns = [
    path('' , home,name='home'),
    path('view_contacts' , viewContacts ,name='viewContacts'),
    path('save_contacts' , saveContacts ,name='saveContacts'),
    path('send_message' , sendMessage ,name='sendMessage'),
    path('message' , messages ,name='messages'),


]

