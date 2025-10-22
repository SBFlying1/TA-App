from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import TASignUpForm
from .forms import TAProfileForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import TAProfile
from .models import TA_User

class SignUpView(CreateView):
    model = TA_User
    form_class = TASignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("profile_new")

class TAProfileCreateView(LoginRequiredMixin, CreateView):
    model = TAProfile
    form_class = TAProfileForm
    template_name = "registration/info_create.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TAProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = TAProfile
    form_class = TAProfileForm
    template_name = "registration/info_edit.html"
    success_url = reverse_lazy("home")
    def get_object(self, queryset=None):
        profile, created = TAProfile.objects.get_or_create(user=self.request.user)
        return profile