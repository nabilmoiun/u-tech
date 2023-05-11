from django.urls import path

from .views import (
    InsertSale,
    RetriveUpdateDeleteSale,
    GenertePdfReport
)

urlpatterns = [
    path('insert-sale/', InsertSale.as_view(), name='create-sale'),
    path('retrieve-update-delete-sale/<int:pk>/', RetriveUpdateDeleteSale.as_view(), name='retrieve-update-delete-sale'),
    path('generate-pdf-report/', GenertePdfReport.as_view(), name='generate-pdf-report'),
]