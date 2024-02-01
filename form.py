from django import forms
from .models import Profile,Reviews

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        
        exclude=['user']


class ReviewForm(forms.ModelForm):
    class Meta:
        model=Reviews
        exclude=['user','post']