from django import forms


# HomeWork 6: Create the form for calculating an hypotenuse
class TriangleForm(forms.Form):
    first_side = forms.IntegerField(min_value=1, required=True, label='Сторона: A', )
    second_side = forms.IntegerField(min_value=1, required=True, label='Сторона: B', )
