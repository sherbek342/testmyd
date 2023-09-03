from .models import Articles 
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput( attrs={
                'class': 'form-control',
                'placeholder': 'Название lifs'
            }),
            "anons": TextInput( attrs={
                'class': 'form-control',
                'placeholder': 'Анонс lifs'
            }),
            "full_text": Textarea( attrs={
                'class': 'form-control',
                'placeholder': 'Lifs'
            }),
            "date": DateTimeInput( attrs={
                'class': 'form-control',
                'placeholder': 'Дата Публикации'
            })
        }