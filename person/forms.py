from datetime import timedelta

from django import forms
from django.utils import timezone

from .models import Person


# HomeWork 7: The form for creating personal data
class NewPerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'age')


# Homework 12. Celery
class ReminderFrom(forms.Form):
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    date = forms.DateTimeField(required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
                               label='Time for reminder')

    def clean_date(self):
        time = self.cleaned_data['date']
        time_now = timezone.now()
        if time <= time_now or time >= time_now + timedelta(days=2):
            raise forms.ValidationError("the date cannot be in the past and the date must be no later than 2 days")
        return time
