from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import TA_User, TAProfile
class TASignUpForm(UserCreationForm): 
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
    COURSE_CHOICES = [
        ("CSCI133", "CSCI 321"),
        ("CSCI233", "CSCI 123"),
        ("CSCI253", "CSCI 253"),
        ("CSCI212", "CSCI 273"),
    ]

    courses = forms.MultipleChoiceField(
        choices=COURSE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    
    class Meta:
        model = TAProfile
        fields = ["availability_start", "availability_end", "description", "courses"]

