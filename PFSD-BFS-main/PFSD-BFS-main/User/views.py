from django.shortcuts import *
from django.core.mail import send_mail
from .models import *
from .forms import *
from .randomnumber import *
from django.db.models import * 
from datetime import *


# Create your views here.

otp_generated=''

forgot_otp_generated=''


# Index page
def index(request):
    return render(request, 'Welcome.html')

#login page
def login(request):
    return render(request, 'Login.html')

#logged in action
def logined(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user_details=User_Details.objects.filter(username=username,password=password).values()
        if user_details:
            krk=list(user_details)
            logined_in_usermail=krk[0]['email']
            logined_in_account_no=krk[0]['account_no']
            if krk[0]['role'] == 'user':
                x=request.session['id1']=logined_in_account_no
                transaction_data=Transaction.objects.filter(Q(toaccountnumber=logined_in_account_no) | Q(fromaccountnumber=logined_in_account_no)).order_by('dateoftransaction')
                count=transaction_data.count()
                rsa=Registration.objects.filter(email=logined_in_usermail).values()
                rsalist=list(rsa)
                rsaname=rsalist[0]['first_name']+" "+rsalist[0]['last_name']
                senderemail=logined_in_usermail
                tosend="you logined today at location"
                # send_mail(
                #         'Login Session Started',
                #          tosend,
                #         'venkatasairamreddy0404@gmail.com',
                #          [senderemail],
                #         fail_silently=False,
                #     )
                print(x)
                return redirect('mpin')
            elif krk[0]['role']=='admin':
                x=request.session['id1']=logined_in_account_no
                return redirect('admin_home')
                 
        else:
            return render(request,'Login.html',{"message":"Invalid Credentials"})

# sign up page
def signup(request):
    return render(request, 'Signup.html')

# signed up action
def registered(request):
    global otp_generated
    global  registration_details
    global  regirstree_email
    if request.method=='POST':
        regirstree_email=request.POST['email']
        registration_details=Registrations_form(request.POST or None)
        fetched_data=Registration.objects.filter(email=regirstree_email)
        if fetched_data:
            return render(request, 'signup.html', {'message': 'Email Already existed'})
        else:
            kk=999999999
            if registration_details.is_valid:
                senderemail=regirstree_email
                otp_generated=otpgen()
                tosend='\n This is the conformation mail here is the OTP : '+otp_generated+'\n please verify your mail'
                send_mail('Thank you for Registering',
                          tosend,
                          'karthikeyavadde@gmail.com',
                          [senderemail],
                          fail_silently=False,
                         )
                print(otp_generated)
                return render(request,'OtpPage.html')
            
# otp page
def otppage(request):
    return render(request, 'OtpPage.html')

# otp confirmation
def otpconfirmation(request):
    if request.method == 'POST':
        digit1 =request.POST['digit-1']
        digit2 =request.POST['digit-2']
        digit3 =request.POST['digit-3']
        digit4 =request.POST['digit-4']
        digit5 =request.POST['digit-5']
        digit6 =request.POST['digit-6']
        otp_entered=digit1+digit2+digit3+digit4+digit5+digit6
        print(otp_entered,otp_generated)
        if otp_entered== otp_generated :
                registration_details.save()
                user_details=User_Details.objects.create()
                account_details=AccountDetails.objects.create()
                q=User_Details.objects.filter().latest('account_no')
                print(q)
                user_details.account_no=(q.account_no+1)
                user_details.email= regirstree_email
                user_details.verified_status="pending"
                user_details.account_status="active"
                user_details.save()
                rsa=Registration.objects.filter(email=regirstree_email)
                rsalist=list(rsa.values())
                accountholder=rsalist[0]['first_name']+" "+rsalist[0]['last_name']
                account_details.accountholder=accountholder
                account_details.accountnumber=(q.account_no+1)
                account_details.save()
                user=User_Details.objects.filter(email=regirstree_email)
                user1=list(user.values())
                senderemail=user1[0]['email']
                tosend='Username : '+user1[0]['username']+"\nPassword : "+str(user1[0]['password'])+"\nMPIN : "+str(user1[0]['mpin'])+"\n Please Change username,password and mpin after login"
                send_mail(
                    'Thank you for contacting us',
                     tosend,
                    'venkatasairamreddy0404@gmail.com',
                     [senderemail],
                    fail_silently=False,
                )
                return redirect('login')
        else:
            return render(request,'OtpPage.html',{'message': 'Incorrect Otp Please Check your mail'})
        return render(request,'Signup.html')
    return render(request,'timeout.html')
    
# forgot password page
def forgotpassword(request):
    return render(request, 'ForgotPassword.html')

def forgotpasswordrequested(request):
    if request.method=='POST':
        global enteredemail
        email=request.POST['email']
        enteredemail=email
        new_password=request.POST['password']
        global new_pass
        new_pass=new_password
        fetched_data=User_Details.objects.filter(email=email)
        if fetched_data:
            senderemail=email
            otp_generate=''.join(random.sample(string.digits,6))
            global forgot_otp_generated
            forgot_otp_generated=otp_generate
            print(forgot_otp_generated)
            tosend='\n This is the password update mail here is the OTP : '+otp_generate+'\n'
            send_mail('Thank you for Registering',
                          tosend,
                         'venkatasairamreddy0404@gmail.com',
                          [senderemail],
                          fail_silently=False,
                         )
            return render(request, 'forgot_password_otp.html')
    return render(request,'timeout.html')

def forgotpasswordotpconfirmation(request):
    if request.method == 'POST':
        digit1 =request.POST['digit-1']
        digit2 =request.POST['digit-2']
        digit3 =request.POST['digit-3']
        digit4 =request.POST['digit-4']
        digit5 =request.POST['digit-5']
        digit6 =request.POST['digit-6']
        otp_entered=digit1+digit2+digit3+digit4+digit5+digit6
        print("'",otp_entered,"'",forgot_otp_generated)
        if otp_entered== forgot_otp_generated :
                rr=User_Details.objects.filter(email=enteredemail)
                rr.update(password=new_pass)
                return redirect('login')
        else:
            return render(request,'forgot_password_otp.html',{'message': 'Incorrect Otp Please Check your mail'})

    return render(request,'timeout.html')



#mpin page 
def mpin(request):
    return render(request, 'MPIN.html')

def admin_home(request):
    if 'id1' in request.session:
        rr=Registration.objects.all()
        count=rr.count()
        return render(request, 'admin/view_user.html',{'count':count,'users':rr})
    else:
        return render(request, 'timeout.html')

def transfer(request):
    if 'id1' in request.session:
        x=request.session['id1']
        rr=User_Details.objects.get(account_no=x)
        rsa=Registration.objects.filter(email=rr.email)
        rsalist=list(rsa.values())
        rsaname=rsalist[0]['first_name']+" "+rsalist[0]['last_name']
        accountnumber=rr.account_no
        transaction_data=Transaction.objects.filter(Q(toaccountnumber=accountnumber) | Q(fromaccountnumber=accountnumber)).order_by('-dateoftransaction','-timeoftransaction')
        return render(request,'Transfer.html',{'accountnumber':accountnumber,'name':rsaname,'data':transaction_data})
    else:
        return render(request,'timeout.html')



def dashboard(request):
    if 'id1' in request.session:
        rr=User_Details.objects.filter(account_no=request.session['id1'])
        krk=list(rr.values())
        rsa=Registration.objects.filter(email=krk[0]['email'])
        rsalist=list(rsa.values())
        rsaname=rsalist[0]['first_name']+" "+rsalist[0]['last_name']
        accountdetails=AccountDetails.objects.get(accountnumber=request.session['id1'])
        transaction_data=Transaction.objects.filter(Q(toaccountnumber=request.session['id1']) | Q(fromaccountnumber=request.session['id1'])).order_by('-dateoftransaction','-timeoftransaction')
        return render(request, 'Dashboard.html',{'name':rsaname,'data':transaction_data,'balance':accountdetails.balance})
    else:
        return render(request, 'timeout.html')

def transactions(request):
     if 'id1' in request.session:
        x=request.session['id1']
        rr=User_Details.objects.filter(account_no=x)
        krk=list(rr.values())
        kmp=krk[0]['email']
        account_number=krk[0]['account_no']
        print(account_number)
        transaction_data=Transaction.objects.filter(Q(toaccountnumber=account_number) | Q(fromaccountnumber=account_number)).order_by('-dateoftransaction','-timeoftransaction')
        count=transaction_data.count()
        chart_debit_data=transaction_data.filter(toaccountnumber=account_number).values('month').annotate(balance=Sum('amount')).order_by('-month')
        chart_credit_data=transaction_data.filter(fromaccountnumber=account_number).values('month').annotate(balance=Sum('amount')).order_by('-month')
        chart_purpose_data=transaction_data.filter(Q(month=calendar.month_name[datetime.now().month])).values('purpose').annotate(balance=Sum('amount')).order_by('-purpose')
        monthly_debit=chart_debit_data.filter(Q(month=calendar.month_name[datetime.now().month]))
        monthly_credit=chart_credit_data.filter(Q(month=calendar.month_name[datetime.now().month]))
        print(monthly_debit)
        print(monthly_credit)


        # print(chart_debit_data)
        # print(chart_credit_data)
        print(chart_purpose_data)

        rsa=Registration.objects.filter(email=kmp)
        rsalist=list(rsa.values())
        rsaname=rsalist[0]['first_name']+" "+rsalist[0]['last_name']
        return render(request, "Transactions.html",{'name':rsaname,'data':transaction_data,'count':count,'chart_purpose_data':chart_purpose_data,'chart_debit_data':chart_debit_data,'chart_credit_data':chart_credit_data})
     else:
        return render(request, 'timeout.html')



def signout(request):
    request.session.flush()
    return redirect('login')
    



def transfered(request):
        if request.method=='POST':
            to_account=request.POST['to_account']
            from_account=request.POST['from_account']
            amount=request.POST['amount']
            r=AccountDetails.objects.get(accountnumber=from_account)
            if r.balance >= float(amount):
                transfer=Transaction.objects.create()
                transfer.toaccountnumber=to_account
                transfer.fromaccountnumber=from_account
                transfer.amount=amount
                transfer.purpose=request.POST['purpose']
                transfer.status='Success'
                k=AccountDetails.objects.get(accountnumber=to_account)
                print(r,k)
                r.balance=(r.balance-float(amount))
                k.balance=(k.balance+float(amount))
                r.save()
                k.save()
                transfer.save()
                return redirect('transfer')
            else:
                return render(request,'InsufficentFunds.html')

def change_credintials(request):
    return render(request, 'change_credintials.html')

def savings(request):
    if 'id1' in request.session:
        rr=AccountDetails.objects.get(accountnumber=request.session['id1'])
        return render(request,'Savings.html',{'savings':rr.savings,'tosave':rr.tosave})
    else:
        return render(request,'timeout.html')


def savings_saved(request):
     if 'id1' in request.session:
        if request.method == 'POST':
            amount = request.POST['amount']
            rr=AccountDetails.objects.get(accountnumber=request.session['id1'])
            if rr.balance <= float(amount):
                return render(request,'InsufficentFunds.html')
            else:
                rr.savings=rr.savings+float(amount)
                rr.balance=rr.balance-float(amount)
                rr.save()
                transfer=Transaction.objects.create()
                transfer.toaccountnumber=request.session['id1']
                transfer.fromaccountnumber=request.session['id1']
                transfer.amount=amount
                transfer.purpose='Savings'
                transfer.status='Success'
                transfer.save()
                print(rr.savings)
                return redirect('savings')   


def loans(request):
    if 'id1' in request.session:
        data=LoansDetails.objects.filter(applier_account_no=request.session['id1'])
        return render(request,'Loans.html',{'data':data})
    else:
        return render(request, 'timeout.html')


def cards(request):
    if 'id1' in request.session:
        cardsdata=CardDetails.objects.filter(accountnumber=request.session['id1'])
        count =cardsdata.count()
        Account_Details=AccountDetails.objects.get(accountnumber=request.session['id1'])
        return render(request,'Cards.html',{'count':count,'cards':cardsdata,'balance':Account_Details.balance})
    else:
        return render(request, 'timeout.html')


def card_requested(request):
    if 'id1'in request.session:
        if request.method == 'POST':
            card_type=request.POST['category']
            cardsdata=CardDetails.objects.filter(accountnumber=request.session['id1'])
            count =cardsdata.count()
            if count >= 2 :
                return HttpResponse("Card limit exceeded")
            if card_type=='':
                return HttpResponse('Invalid card type')
            print(request.session['id1'])
            fetched_data=User_Details.objects.get(account_no=request.session['id1'])
            rr=Registration.objects.get(email=fetched_data.email)
            rsaname=rr.first_name+" "+rr.last_name
            print(rsaname)
            card_details=CardDetails.objects.create()
            card_details.accountnumber=request.session['id1']
            card_details.cardtype=card_type
            card_details.cardnumber=cardnumbergen()
            card_details.cardholder=rsaname
            card_details.cardstatus='active'
            card_details.verificationstatus='pending'
            card_details.save()
            print(card_type)
            return redirect('cards')
    else:
        return render(request, 'timeout.html')

def applyloans(request):
    return render(request,'Applyloan.html')


def appliedloan(request):
     if 'id1' in request.session: 
        if request.method == 'POST':
            occupation = request.POST['occupation']
            annualincome = request.POST['annualincome']
            purpose=request.POST['purpose']
            category=request.POST['category']
            loanamount=request.POST['loanamount']
            print(occupation,annualincome,purpose,loanamount)
            loan_request=LoansDetails.objects.create()
            loan_request.applier_account_no=request.session['id1']
            loan_request.amount=loanamount
            loan_request.interest=calculate_interest(category)
            loan_request.occupation=occupation
            loan_request.totalPayment=loanamount
            loan_request.monthlyPayment=float(loanamount)/10
            loan_request.loan_category=category
            loan_request.annual_income=annualincome
            loan_request.purpose_of_loan=purpose
            loan_request.save()



            return redirect('loans')
        

def pinconfirmation(request):
    if request.method == 'POST':
        digit1 =request.POST['digit-1']
        digit2 =request.POST['digit-2']
        digit3 =request.POST['digit-3']
        digit4 =request.POST['digit-4']
        pin_entered=digit1+digit2+digit3+digit4
        user_details=User_Details.objects.get(account_no=request.session['id1'])
        if int(pin_entered)== user_details.mpin:
            return redirect('dashboard')
        else:
            senderemail=user_details.email
            tosend="You have Your MPIN correctly if it is not done by you please contact us"
            send_mail(
                    'Thank you for contacting us',
                     tosend,
                    'venkatasairamreddy0404@gmail.com',
                     [senderemail],
                    fail_silently=False,
                )
            return render(request, 'MPIN.html',{'message':'Incorrect MPin Try Again'})
        
def delete_user(request,uemail):
    ud=User_Details.objects.get(email=uemail)
    if ud.role == 'admin':
        return redirect("admin_home")
    else :
        Registration.objects.filter(email=uemail).delete()
        ud=User_Details.get(email=uemail)
        acc_no=ud.account_no
        User_Details.filter(accountnumber=acc_no).delete()
        AccountDetails.filter(accountnumber=acc_no).delete()
        return HttpResponse("Deleted the User and its Account")  