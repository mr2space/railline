from django.urls import path
from . import views
urlpatterns = [
    # path('',views.accounts,name="accounts"),
    path('',views.accountsViews.as_view(),name="our first API")
]
