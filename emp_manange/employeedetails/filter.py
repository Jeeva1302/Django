from django import forms
import django_filters

from employeedetails.models import Employee

class Empfilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ['Firstname', 'State', 'streetadress', 'Experience']

    # Set placeholders for each field    
    Firstname = django_filters.CharFilter(lookup_expr='icontains', label='Firstname', widget=forms.TextInput(attrs={'placeholder': 'Enter Firstname'}))
    State = django_filters.CharFilter(lookup_expr='icontains', label='State', widget=forms.TextInput(attrs={'placeholder': 'Enter State'}))
    streetadress = django_filters.CharFilter(lookup_expr='icontains', label='Street Address', widget=forms.TextInput(attrs={'placeholder': 'Enter Street Address'}))
    Experience = django_filters.CharFilter(lookup_expr='icontains', label='Experience', widget=forms.TextInput(attrs={'placeholder': 'Enter Experience'}))
