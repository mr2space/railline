from django.urls import path
from . import views as user_views
urlpatterns = [
    # path('',views.accounts,name="accounts"),
    path('register', user_views.userRegistration.register, name='register'),
    path('verifyEmail', user_views.userRegistration.verifyEmail,name='verfyEmail'),
    # path('api',user_views.accountsViews.as_view(),name="our first API")
]
