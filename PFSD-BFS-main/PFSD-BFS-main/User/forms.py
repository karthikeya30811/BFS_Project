from django import forms

from .models import *

class Registrations_form(forms.ModelForm):
    class Meta:
        model=Registration
        fields=['first_name','last_name','father_name','mother_name','dob','gender','phone','email','aadharnumber','pannumber','pincode']

class user_form(forms.ModelForm):
    class Meta:
        model=User_Details
        fields=['email']

class card_form(forms.ModelForm):
    class Meta:
        model=CardDetails
        fields=['accountnumber','cardtype','cardnumber','cardholder','cvv','issueddatetime','expirydatetime','cardstatus','verificationstatus']
