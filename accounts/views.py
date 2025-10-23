from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import TASignUpForm, TAProfileForm, AvailabilitySlotForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import TAProfile, TA_User, AvailabilitySlot
from django.shortcuts import redirect
from django.forms import inlineformset_factory
from datetime import datetime, timedelta
from django.utils import timezone
from django.shortcuts import render

class SignUpView(CreateView):
    model = TA_User
    form_class = TASignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("profile_edit")

AvailabilitySlotFormSet = inlineformset_factory(
    TAProfile,
    AvailabilitySlot,
    form=AvailabilitySlotForm,
    extra=1,  
    can_delete=True, 
    min_num=0 
)

class TAProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = TAProfile
    form_class = TAProfileForm
    template_name = "registration/info_edit.html"
    success_url = reverse_lazy("home")
    def get_object(self, queryset=None):
        profile, created = TAProfile.objects.get_or_create(user=self.request.user)
        return profile
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        if self.request.POST:
            context['slot_formset'] = AvailabilitySlotFormSet(
                self.request.POST, instance=self.object
            )
        else:
            context['slot_formset'] = AvailabilitySlotFormSet(instance=self.object)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        slot_formset = AvailabilitySlotFormSet(request.POST, instance=self.object)
        if form.is_valid() and slot_formset.is_valid():
            form.save()
            slot_formset.save()
            if 'save_exit' in request.POST:
                return redirect('home') 
            else:
                return redirect('profile_edit')
        context = self.get_context_data(form=form)
        context['slot_formset'] = slot_formset
        return self.render_to_response(context)
    
def ta_profile_detail(request, pk):
    profile = TAProfile.objects.get(pk=pk)
    slots = AvailabilitySlot.objects.filter(profile=profile).order_by('day', 'start_time')
    return render(request, "registration/ta_profile_detail.html", {"profile": profile, "slots": slots})

DAY_MAP = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6,
}

def all_ta_availability(request):
    now = timezone.localtime()
    current_weekday = now.weekday()
    slots = AvailabilitySlot.objects.select_related('profile__user')
    def next_occurrence(slot):
        slot_weekday = int(slot.day)
        days_ahead = (slot_weekday - current_weekday) % 7
        slot_date = now.date() + timedelta(days=days_ahead)
        slot_datetime = datetime.combine(slot_date, slot.start_time)
        if days_ahead == 0 and slot.start_time < now.time():
            slot_datetime += timedelta(days=7)
        return timezone.make_aware(slot_datetime)
    sorted_slots = sorted(slots, key=next_occurrence)
    return render(request, 'registration/all_ta_availability.html', {'sorted_slots': sorted_slots})