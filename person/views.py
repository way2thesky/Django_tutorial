from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import NewPerson, ReminderFrom
from .models import Person


# Homework 7. Django: Создание и обновление персональных данных в БД
def create_person_data(request):
    if request.method == "POST":
        form = NewPerson(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Created")
            return redirect(reverse('person:update_person', args=(instance.pk,)))
        else:
            messages.error(request, 'Not Created')
    else:
        form = NewPerson()
    context = {
        'form': form,
    }
    return render(request, '../templates/create_data.html', context)


def update_person_data(request, pk=None):  # noqa A002
    instance = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = NewPerson(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Saved!")
            return redirect(reverse('person:update_person', args=(instance.pk,)))
    else:
        form = NewPerson(instance=instance)
    context = {
        'form': form,
        'person_upd': instance,
    }
    return render(request, '../templates/update_data.html', context)


# def reminder_form(request):
#     if request.methed == "POST":
#         form = ReminderFrom()
#     else:
#         form = ReminderFrom(request.POST)
#         if form.is_valid():
#             subject = 'Напоминание'
#             message = form.cleaned_data['message']
#             from_email = form.cleaned_data['from_email']
#             text = form.cleaned_data['text']
#             data_rem = form.cleaned_data['reminder']
#             try:
