from django.urls import path
from . import views
urlpatterns = [
    path("", views.userBooking),
    path("payment-pre-process", views.paymentPreProcess, name="payment-pre-process"),
    path("success",views.success,name="success"),
    path("cancel",views.cancel,name="cancel"),
    path("payment_webhook_view", views.payment_webhook_view,
         name="payment_webhook_view")
]
