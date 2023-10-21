from django.urls import path
from .views import StoresByPhoneNumber, CreateVisit

urlpatterns = [
    path('stores/<str:phone_number>/', StoresByPhoneNumber.as_view(), name='stores-by-phone'),
    path('create-visit/', CreateVisit.as_view(), name='create-visit'),
]
