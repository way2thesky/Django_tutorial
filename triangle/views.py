import math

from django.shortcuts import render

from .forms import TriangleForm


# Homework 6. Django: Калькулятор гипотенузы
def triangle(request):
    if request.method == "POST":
        form = TriangleForm(request.POST)
        if form.is_valid():
            first_side = form.cleaned_data['first_side']
            second_side = form.cleaned_data['second_side']
            gip = math.sqrt(first_side ** 2 + second_side ** 2)
            return render(request, "../templates/form_triangle.html", context={'gip': gip})
    else:
        form = TriangleForm()
    return render(request, "../templates/form_triangle.html", context={"form": form})
