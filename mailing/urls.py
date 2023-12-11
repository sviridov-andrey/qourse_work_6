from django.urls import path

from .apps import MailingConfig
from .views import MailingListView, MailingCreateView, ClientCreateView, MailingUpdateView, \
    MailingDeleteView, MailingDetailView, ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView, \
    IndexListView

app_name = MailingConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingCreateView.as_view(), name='create'),
    path('update/<int:pk>/', MailingUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', MailingDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='delete'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    ]
