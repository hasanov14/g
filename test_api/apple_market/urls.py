from django.urls import path
from .views import *

urlpatterns = [
    path('phones/', TelephoneList.as_view()),
    path('phones/create/', TelephoneCreate.as_view()),
    path('phones/update/<int:pk>/', TelephoneUpdate.as_view()),
    path('phones/mixed/', TelephoneMixed.as_view()),
    path('phones/<int:pk>/', TelephoneDetail.as_view()),
    path('phones/delete/<int:pk>/', TelephoneDelete.as_view())
]
