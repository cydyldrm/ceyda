from .views import contact_form, contact
from django.urls import path

urlpatterns = [
    path('contact_form', contact_form, name='contact_form'),
    path('contact', contact, name='contact'),
]
