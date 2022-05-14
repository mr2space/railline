from django.urls import path
from . import views
urlpatterns = [
    path("api/<train_no>/<id>", views.userBooking),
]
