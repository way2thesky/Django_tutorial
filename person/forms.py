from django import forms

from .models import Person


# HomeWork 7: The form for creating personal data
class NewPerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'age')
