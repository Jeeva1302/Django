from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name="index") ,
    path('insert', views.insertdata, name="insertdata"),
    path('update/<id>', views.updatedata, name="updatedata"),
    path('delete/<id>', views.deletedata, name="deletedata"),
    path('filter/', views.filterdata, name="filterdata")
    
]