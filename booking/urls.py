from django.urls import path
from . import views
urlpatterns = [
    path("api/booking/<train_no>/<destination>/<boarding>/<id>", views.userBooking)
]
