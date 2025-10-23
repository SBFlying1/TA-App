from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import TA_User, TAProfile, AvailabilitySlot
class TASignUpForm(UserCreationForm): 
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta: 
        model = TA_User
        fields = (
            "first_name",
            "last_name",
            "username", 
            "email", 
            "password1",
            "password2",
        )

class TAProfileForm(forms.ModelForm):
    courses = forms.MultipleChoiceField(
        choices=TAProfile.COURSE_CHOICES,
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )
    
    class Meta:
        model = TAProfile
        fields = ["description", "courses"]

class AvailabilitySlotForm(forms.ModelForm):
    class Meta:
        model = AvailabilitySlot
        fields = ['day', 'start_time', 'end_time']
        widgets = {
            'day': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.Select(attrs={'class': 'form-control'}),
            'end_time': forms.Select(attrs={'class': 'form-control'}),
        }
