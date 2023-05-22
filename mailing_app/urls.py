from django.urls import path
from mailing_app.apps import MailingAppConfig
from mailing_app.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, \
    MailingDeleteView, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = MailingAppConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing_update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
]
