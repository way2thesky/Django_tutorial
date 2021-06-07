from django import forms

from .models import Person


# HomeWork 6: Create the form for calculating an hypotenuse
class TriangleForm(forms.Form):
    first_side = forms.IntegerField(min_value=1, required=True, label='Сторона: A', )
    second_side = forms.IntegerField(min_value=1, required=True, label='Сторона: B', )


# HomeWork 7: The form for creating personal data
class NewPerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'age')
