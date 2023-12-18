from django import forms
from mailing.models import Mailing, Client
import datetime


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'clients':
                continue
            elif field_name == 'user':
                continue
            elif field_name == 'is_active':
                continue
            else:
                field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):
    clients = forms.CheckboxSelectMultiple()
    # time_start = forms.DateTimeField()
    # time_end = forms.DateTimeField()

    class Meta:
        model = Mailing
        exclude = ['user', 'is_active']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['clients'].queryset = Client.objects.filter(user=user)

    def clean_day(self):
        cleaned_data = self.cleaned_data['day']

        if 0 > cleaned_data > 31:
            raise forms.ValidationError('Число должно быть от 1 до 31')

        return cleaned_data


class MailingUpdateForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        exclude = ['is_active']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['clients'].queryset = Client.objects.filter(user=user)
        self.fields['user'].disabled = True


class MailingManagerUpdateForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        exclude = ['clients']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].disabled = True
        self.fields['body'].disabled = True
        self.fields['status'].disabled = True
        self.fields['time_start'].disabled = True
        self.fields['time_end'].disabled = True
        self.fields['periodicity'].disabled = True
        self.fields['day'].disabled = True
        self.fields['day_week'].disabled = True
        self.fields['user'].disabled = True


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('user',)
