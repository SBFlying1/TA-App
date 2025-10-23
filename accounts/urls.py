from django.urls import path
from .views import SignUpView, TAProfileUpdateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/edit/", TAProfileUpdateView.as_view(), name="profile_edit"),
]