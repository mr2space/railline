from django.urls import path
from . import views
urlpatterns = [
    path("", views.userBooking),
    path("payment-pre-process", views.paymentPreProcess, name="payment-pre-process"),
    path("success",views.success,name="success"),
    path("cancel",views.cancel,name="cancel"),
    path("payment-test", views.paymentTest, name="paymentTest"),
    path("payment_webhook_view", views.stripeWebhook,
         name="payment_webhook_view")
]
