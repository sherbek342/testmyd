from .models import Profile
from django.forms import ModelForm, TextInput

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['ptitle']
        widgets = {
            'ptitle': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            })
        }