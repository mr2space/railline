from django.urls import path
from . import views
urlpatterns = [
    path("", views.userBooking),
    path("payment-pre-process", views.userBooking, name="payment-pre-process")
]
