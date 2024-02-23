from django.urls import path
from django.views.generic import TemplateView

from sampleoperation.views import create_user

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('create_user/', create_user, name='create_user'),
]