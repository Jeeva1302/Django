from django import forms
from django.shortcuts import redirect, render

from employeedetails.filter import Empfilter
from .models import Employee

# Create your views here.

def index(request):
    data = Employee.objects.all()
    context = {"data":data}
    return render(request, 'index.html', context)


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Firstname', 'Lastname', 'Qualification', 'Experience', 'Email', 'Phonenumber', 'streetadress', 'State', 'Country', 'Zipcode', 'Areacode']

    def clean_Firstname(self):
        firstname = self.cleaned_data.get('Firstname')
        if Employee.objects.filter(Firstname=firstname).exists():
            raise forms.ValidationError("This name is already registered.")
        return firstname

    def clean_Email(self):
        email = self.cleaned_data.get('Email')
        if Employee.objects.filter(Email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean_Phonenumber(self):
        phonenumber = self.cleaned_data.get('Phonenumber')
        if Employee.objects.filter(Phonenumber=phonenumber).exists():
            raise forms.ValidationError("This phone number is already registered.")
        return phonenumber

def insertdata(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeForm()

    return render(request, 'index.html', {'form': form})
    

def updatedata(request, id):
       if request.method == "POST":  
        Firstname = request.POST['Firstname']
        Lastname  = request.POST['Lastname']
        Qualification = request.POST['Qualification']
        Experience = request.POST['Experience']
        Email = request.POST['Email']
        Phonenumber= request.POST['Phonenumber']
        streetadress= request.POST['streetadress']
        State = request.POST['State']
        Country = request.POST['Country']
        Zipcode= request.POST['Zipcode']
        Areacode= request.POST['Areacode']
        
        edit = Employee.objects.filter(id = id).update('')
        
        edit.Firstname = Firstname
        edit.Lastname = Lastname
        edit.Experience = Experience
        edit.Qualification = Qualification
        edit.streetadress = streetadress
        edit.State = State
        edit.Country = Country
        edit.Zipcode = Zipcode
        edit.Areacode = Areacode
        edit.Email = Email
        edit.Phonenumber = Phonenumber
        edit.save()
        
        return redirect('/')
    
    
       d = Employee.objects.get(id = id)
       context = {"d":d}
       return render(request, 'update.html', context)
    
    
def deletedata(request, id):
    d = Employee.objects.get(id = id)
    d.delete()
    return redirect('/')


def filterdata(request):
    # Get filter criteria from the request
    Firstname = request.GET.get('Firstname', '')
    Lastname = request.GET.get('Lastname', '')
    Qualification = request.GET.get('Qualification', '')
    Experience = request.GET.get('Experience', '')
    Email = request.GET.get('Email', '')
    Phonenumber = request.GET.get('Phonenumber', '')
    streetadress = request.GET.get('streetadress', '')
    State = request.GET.get('State', '')

    # Fetch all employees initially
    employees = Employee.objects.all()

    # Create a filter instance with the provided criteria
    myfilter = Empfilter(request.GET, queryset=employees)

    # Apply the filter to the queryset
    filtered_employees = myfilter.qs

    # You can print or use filtered_employees as needed

    context = {
        'Firstname': Firstname,
        'Lastname': Lastname,
        'Qualification': Qualification,
        'Experience': Experience,
        'Email': Email,
        'Phonenumber': Phonenumber,
        'streetadress': streetadress,
        'State': State,
        'myfilter': myfilter,
        'filtered_employees': filtered_employees,
    }

    return render(request, 'filter.html', context)