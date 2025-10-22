from django.urls import path
from .views import SignUpView, TAProfileCreateView, TAProfileUpdateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/new/", TAProfileCreateView.as_view(), name="profile_new"),
    path("profile/edit/", TAProfileUpdateView.as_view(), name="profile_edit"),
]