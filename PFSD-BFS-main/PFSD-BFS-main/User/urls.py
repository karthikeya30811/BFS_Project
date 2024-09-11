from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('forgotpass',views.forgotpassword,name='forgotpassword'),
    path('otp',views.otppage,name='otppage'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('transaction',views.transactions,name='transaction'),
    path('registered',views.registered,name='registered'),
    path('logined',views.logined,name='logined'),
    path('signout',views.signout,name='signout'),
    path('transfer',views.transfer,name='transfer'),
    path('otpconfirmation',view=views.otpconfirmation,name='otpconfirmation'),
    path('pinconfirmation',view=views.pinconfirmation,name='pinconfirmation'),
    path('transferred',views.transfered,name='transfered'),
    path('savings',views.savings,name='savings'),
    path('savings_saved',views.savings_saved,name='savings_saved'),
    path('loans',views.loans,name='loans'),
    path('cards',views.cards,name='cards'),
    path('applyloans',views.applyloans,name='applyloans'),
    path('appliedloan',views.appliedloan,name='appliedloan'),
    path('card_requested',views.card_requested,name='card_requested'),
    path('mpin',views.mpin,name='mpin'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('forgotpasswordrequested',views.forgotpasswordrequested,name='forgotpasswordrequested'),
    path('forgotpasswordotpconfirmation',views.forgotpasswordotpconfirmation,name='forgotpasswordot'),
    path("user/deleteuser/<str:uemail>",views.delete_user,name="user/deleteuser"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)