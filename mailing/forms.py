from django import forms
from django.http import request
from mailing.models import Mailing, Client
from config import settings
from users.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'clients':
                continue
            else:
                field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):
    clients = forms.CheckboxSelectMultiple()
 #   user = forms.ChoiceField(label='uzver')

    class Meta:
        model = Mailing
        fields = '__all__'
       # exclude = ('user', 'is_active',)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = kwargs.pop('user', user)
        self.fields['user'] = self.user
        self.fields['clients'].queryset = Client.objects.filter(user=user)


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
      #  exclude = ('user',)
