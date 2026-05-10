from django import forms
from .models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = [
            'tamil_word',
            'arabic_word',
            'category',
            'example_sentence',
        ]

        widgets = {
            'tamil_word': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Tamil word'
            }),
            'arabic_word': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Arabic word',
                'dir': 'rtl'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'example_sentence': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Example sentence'
            }),
        }