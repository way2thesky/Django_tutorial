import math

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .forms import NewPerson, TriangleForm
from .models import Choice, Person, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# Homework 6. Django: Калькулятор гипотенузы
def triangle(request):
    if request.method == "POST":
        form = TriangleForm(request.POST)
        if form.is_valid():
            first_side = form.cleaned_data['first_side']
            second_side = form.cleaned_data['second_side']
            gip1 = first_side ** 2
            gip2 = second_side ** 2
            gip = math.sqrt(gip1 + gip2)
            return render(request, "polls/form_triangle.html", context={'gip': gip})
    else:
        form = TriangleForm()
    return render(request, "polls/form_triangle.html", context={"form": form})


# Homework 7. Django: Создание и обновление персональных данных в БД
def create_person_data(request):
    form = NewPerson(request.POST)
    if form.is_valid():
        instance = form.save()
        messages.success(request, "Created")
        return redirect(instance.get_absolute_url())
    else:
        messages.error(request, 'Not Created')
    context = {
        'form': form,
    }
    return render(request, 'polls/create_data.html', context)


def update_person_data(request, id=None): # noqa 33
    instance = get_object_or_404(Person, id=id)
    if request.method == "POST":
        form = NewPerson(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Saved!")
            return redirect(reverse('update_person', args=[id]))
    else:
        form = NewPerson(instance=instance)
        context = {
                'form': form,
                'person_upd': instance,
            }
    return render(request, 'polls/update_data.html', context)
