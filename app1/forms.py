from django import forms
from app1.models import *


class HospitalsForm(forms.ModelForm):
    class Meta:
        model = Hospitals
        fields=['hospital_id','password']      


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields=['name','father_name','mother_name','permanent_address','current_address','email','mobile_numbe','blood_group',
        'password','gender','hospital_id','image']