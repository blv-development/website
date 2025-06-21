from django.urls import path
from .views import endorsement_list

urlpatterns = [
    path('', endorsement_list, name='endorsements'),
]