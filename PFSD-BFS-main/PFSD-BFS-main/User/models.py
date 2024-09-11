from django.db import models
import datetime
from . import randomnumber
from django.utils.timezone import *
import calendar
# Create your models here.
class Registration(models.Model):
    first_name=models.TextField(max_length=30)
    last_name=models.TextField(max_length=30)
    father_name=models.TextField(max_length=30)
    mother_name = models.TextField(max_length=30)
    dob=models.DateField()
    gender=models.TextField(max_length=30)
    phone=models.BigIntegerField()
    email=models.EmailField(primary_key=True)
    aadharnumber=models.BigIntegerField()
    pannumber=models.TextField(max_length=10)
    pincode=models.BigIntegerField()
    dateofcreation=models.DateField(default=datetime.date.today())
    profile_pic=models.FileField(blank=False,upload_to="profile_pictures/",null=True)

    def __str__(self):
        return str(self.first_name)+' '+str(self.last_name)+' '+str(self.father_name)+' '+str(self.mother_name)+' '+str(self.dob)+' '+str(self.gender)+' '+str(self.phone)+' '+str(self.email)+' '+str(self.aadharnumber)+' '+str(self.pannumber)+' '+str(self.pincode)+' '+str(self.dateofcreation)
    
class User_Details(models.Model):
    account_no=models.BigIntegerField(default=0)
    email=models.EmailField(default="hii@gmail.com")
    role=models.TextField(default="user",null=True)
    username=models.TextField(default=str(randomnumber.usergen()))
    password=models.TextField(default=str(randomnumber.passgen()))
    mpin=models.BigIntegerField(default=str(randomnumber.pingen()))
    verified_status=models.TextField(null=True)
    account_status=models.TextField(null=True)
    idx=models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.account_no)+' '+str(self.email)+' '+str(self.role)+' '+str(self.username)+' '+str(self.password)+' '+str(self.mpin)+' '+str(self.verified_status)+' '+str(self.account_status)+' '+str(self.idx)

class Transaction(models.Model):
    toaccountnumber=models.BigIntegerField(null=True)
    fromaccountnumber=models.BigIntegerField(null=True)
    amount=models.FloatField(null=True,blank=True)
    purpose=models.TextField(default="transfer")
    status=models.TextField(null=True)
    dateoftransaction=models.DateField(default=str(datetime.date.today()))
    timeoftransaction=models.TimeField(default=str(datetime.datetime.now().time()))
    location=models.TextField(null=True)
    cardnumber=models.BigIntegerField(null=True)
    transaction_id=models.AutoField(primary_key=True)
    month=models.TextField(default=str(calendar.month_name[datetime.datetime.now().month]))

    def __str__(self):
        return str(str(self.toaccountnumber)+' '+str(self.fromaccountnumber)+' '+str(self.amount)+' '+str(self.purpose)+' '+str(self.status)+' '+str(self.dateoftransaction)+' '+str(self.timeoftransaction)+' '+str(self.location)+' '+str(self.cardnumber)+' '+str(self.transaction_id)+' '+str(self.month))

class CardDetails(models.Model):
    accountnumber=models.BigIntegerField(default=0)
    cardtype=models.CharField(max_length=50)
    credit_balance=models.FloatField(default=0.0)
    cardnumber=models.BigIntegerField(null=True)
    cardholder=models.CharField(max_length=100)
    cvv=models.IntegerField(default=randomnumber.cvvgen())
    issueddatetime=models.DateField(default=datetime.date.today())
    expirydatetime=models.DateField(default=datetime.date.today())
    cardstatus=models.CharField(max_length=100)
    verificationstatus=models.CharField(max_length=100)
    cardid=models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.accountnumber+' '+self.cardholder+' '+str(self.cvv)+' '+str(self.issueddatetime)+' '+str(self.expirydatetime)+' '+str(self.cardstatus)+' '+str(self.verificationstatus)+' '+str(self.cardid))
    

class AccountDetails(models.Model):
    accountnumber=models.BigIntegerField(null=True)
    accountholder=models.TextField(max_length=100)
    balance=models.FloatField(default=0.0)
    savings=models.FloatField(default=0.0)
    tosave=models.FloatField(default=0.0)

    def __str__(self):
        return str(str(self.accountnumber)+' '+self.accountholder+' '+str(self.balance)+' '+str(self.savings)+' '+str(self.tosave))


class LoansDetails(models.Model):
    loan_id=models.AutoField(primary_key=True)
    applier_account_no=models.BigIntegerField(null=True)
    tenure=models.IntegerField(null=True, blank=True,default=5)
    amount=models.FloatField(default=0.0)
    interest=models.FloatField(default=0.0)
    totalPayment=models.FloatField(default=0.0)
    monthlyPayment=models.FloatField(default=0.0)
    loan_category=models.CharField(null=True, blank=True,max_length=50)
    occupation=models.CharField(max_length=50,null=True)
    annual_income=models.IntegerField(default=0.0)
    purpose_of_loan=models.CharField(max_length=150,null=True)
    status=models.CharField(max_length=15,default='pending')
    applied_date=models.DateField(datetime.date.today(),null=True)

    def __str__(self):
        return str(self.loan_id+'-'+self.purpose_of_loan+' '+self.status+' '+self.applied_date+' '+self.status+' '+self.applied_date)
   







