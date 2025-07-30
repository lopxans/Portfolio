from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'contact_number', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'forms-control'}),
            'email': forms.EmailInput(attrs={'class': 'forms-control'}),
            'number': forms.TextInput(attrs={'class': 'forms-control'}),
            'message': forms.Textarea(attrs={'class': 'forms-control'}),
        }