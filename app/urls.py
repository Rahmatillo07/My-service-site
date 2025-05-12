from django.urls import path
from .views import add_contact_view

urlpatterns = [
    path('',add_contact_view,name='add')

]