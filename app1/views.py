from django.shortcuts import render,redirect
from app1.forms import *
from app1.models import *
from django.http import HttpResponse
import re
# Create your views here.



def admin_login(request):
    if request.method=='POST':
         form = HospitalsForm(request.POST)
         if form.is_valid():
            hospital_id = request.POST['hospital_id']
            password = request.POST['password']
            obj1 = Hospitals.objects.get(hospital_id= hospital_id)
            if obj1.password==password:
                return render(request,'admin_after_login.html',{'hospital_id' : hospital_id})
            else:
                return HttpResponse("id or password incorrect")
         else:
             return HttpResponse("data invalid")


    else:
        form=HospitalsForm()
        return render(request,'admin_login.html',{'form' : form})



def create_patient_call(request):
    hospital_id = request.POST['hospital_id']
    form=PatientForm()
    return render(request,'create_patient.html',{'hospital_id' : hospital_id , 'form' : form})



def create_patient(request):
    form = EmployeeInformationForm(request.POST)
    print(request.POST)
    if form.is_valid():
        form.instance.patient_id='11111'
        form.save()
        return HttpResponse("data saved")
