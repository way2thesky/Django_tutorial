import datetime  # for checking renewal date range.

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import BookInstance

User = get_user_model()


class RenewBookForm(forms.Form):
    """Form for a librarian to renew books."""
    renewal_date = forms.DateField(
        help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check date is not in past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        # Check date is in range librarian allowed to change (+4 weeks)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data

    class Meta:
        model = BookInstance
        fields = ['due_back', ]
        labels = {'due_back': _('Renewal date'), }
        help_texts = {'due_back': _('Enter a date between now and 4 weeks (default 3).'), }


# action: Это ресурс/URL-адрес куда будут отправлены данные для обработки.
# Если значение не установлено (то есть, значением поля является пустая строка),
# тогда данные будут отправлены в отображение (функцию, или класс), которое сформировало текущую страницу.
# method: HTTP-метод, используемый для отправки данных: post, или get.

# Метод POST должен всегда использоваться если отправка данных приведёт к внесению изменений в базе данных на сервере.
# Применение данного метода должно повысить уровень защиты от CSRF. Метод GET должен применяться только для форм,
# действия с которыми не приводят к изменению базы данных (например для поисковых запросов). Кроме того, данный метод
# рекомендуется применять для создания внешних ссылок на ресурсы сайта. '''


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ContactFrom(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
