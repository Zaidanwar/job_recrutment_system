from django.contrib import admin
from django.urls import path,include
from myapp.views import *


urlpatterns = [

path('',Home.as_view(),name="home"),
path('signup/',Signup.as_view(),name="signup"),
path('fsignup/',FresherSignup.as_view(),name="fsignup"),
path('expsignup/',ExpertSignup.as_view(),name="expsignup"),
path('cmpsignup/',CompanySignup.as_view(),name="cmpsignup"),
path('cmphome/',CompanyHome.as_view(),name="cmphome"),
path('postjob/',PostJob.as_view(),name="postjob"),
path('login/',UserLogin.as_view(),name="login"),
path('userhome/',UserHome.as_view(),name="userhome"),
path('apjob/<int:id>/',AplliedJob.as_view(),name="apjob"),
path('apjoblist/',AplliedJoblist.as_view(),name="apjoblist"),
path('userprofile/',UserProfile.as_view(),name="userprofile"),
path('editprofile/',EditProfile.as_view(),name="editprofile"),
path('viewappl/',ViewApplicants.as_view(),name="viewa"),
path('viewappl/<int:id>',ViewUserinfo.as_view(),name="viewb"),
path('viewac/<int:id>',ViewAcinfo.as_view(),name="viewc"),
path('viewrj/<int:id>',ViewRjinfo.as_view(),name="viewd"),
# path('sendmail/',ViewSendmail.as_view(),name="mail"),


    ]