from django.urls import path
from .views import SignUpView, TAProfileUpdateView
from .views import all_ta_availability

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/edit/", TAProfileUpdateView.as_view(), name="profile_edit"),
    path('availability/', all_ta_availability, name='all_ta_availability')
]