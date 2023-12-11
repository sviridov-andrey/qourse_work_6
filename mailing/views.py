from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import request
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from mailing.forms import MailingForm, ClientForm
from mailing.models import Mailing, Client
from users.models import User


class IndexListView(ListView):
    model = Mailing
    template_name = 'mailing/index.html'
    context_object_name = 'objects_list'


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/mailing_list.html'
    context_object_name = 'objects_list'


class MailingCreateView(PermissionRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy('mailing:mailing_list')
    permission_required = 'mailing.add_mailing'

    def get(self, request, **kwargs):
        form = self.form_class(self.request.user)
        context = {
            'form': form,
        }
        clients = Client.objects.filter(user=self.request.user)
        context['clients'] = clients
        # user = User.objects.filter(email=self.request.user)
        # context['user'] = user
        return render(request, 'mailing/mailing_form.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.user, request.POST)

        if form.is_valid():
            mailing = form.save(commit=False)
            mailing.user = request.user
            mailing.save()
            form.save_m2m()
            return redirect(self.success_url)
        else:
            return render(request, 'mailing/Looser.html')


class MailingUpdateView(PermissionRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy('mailing:index')
    permission_required = 'mailing.change_mailing'


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing/mailing_form.html'


class MailingDeleteView(PermissionRequiredMixin, DeleteView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:index')
    permission_required = 'mailing.delete_mailing'


class ClientCreateView(PermissionRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailing/client_form.html'
    success_url = reverse_lazy('mailing:client_list')
    permission_required = 'mailing.add_client'

    def get_initial(self):
        return {'user': self.request.user}


class ClientListView(PermissionRequiredMixin, ListView):
    model = Client
    template_name = 'mailing/client_list.html'
    context_object_name = 'objects_list'
    permission_required = 'mailing.view_client'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'mailing/client_detail.html'


class ClientUpdateView(PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailing/client_form.html'
    context_object_name = 'objects_list'
    success_url = reverse_lazy('mailing:client_list')
    permission_required = 'mailing.change_client'


class ClientDeleteView(PermissionRequiredMixin, DeleteView):
    model = Client
    template_name = 'mailing/client_delete.html'
    success_url = reverse_lazy('mailing:client_list')
    permission_required = 'mailing.delete_client'
