# from django.http import request
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.views.generic import View
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from datetime import date
from django.core.mail import send_mail
from django.urls import reverse

# Create your views here.
class Home(View):

    def get(self,request):
        return render(request,'homepage.html')

class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        data=request.POST
        employe=data["user"]
        email1=data["email1"]
        user1=data["usn1"]
        passwrd=data["pass1"]
        ph=data["phone"]
        address=data["address"]
        r1=Myuser.objects.create_user(username=user1,password=passwrd,email=email1,address=address,phone_no=ph)

        r1.save()
        user = authenticate(request, username=user1, password=passwrd)
        if user is not None:
            login(request, user)
            if employe=="fresher":
                return redirect('/fsignup/')
            else:
                return redirect('/expsignup/')
        else:
            return HttpResponse("invalid user")

        # if employe=="fresher":
        #     return redirect('/myapp/fsignup/')
        # else:
        #     return render(request,'expertsignup.html')

class FresherSignup(View):
    def get(self,request):
        return render(request,'freshsignup.html')
    def post(self,request):
        data=request.POST
        user=request.user
        # user1=Myuser.objects.get(user_id=user)
        fullname=data["fullname"]
        # address=data["address"]
        gender=data["gender"]
        state = data["state"]
        city = data["city"]
        colllege = data["college"]
        degree = data["degree"]
        spec = data["spec"]
        dob = data["birth_date"]
        f1=FresherRegisterTable(fresher_id=user,full_name=fullname,gender=gender,state=state,city=city,college=colllege,degree=degree,specialization=spec,dob=dob)

        # r2=Myuser(address=address)

        f1.save()
        # r2.save()
        return redirect('/login/')
#
class ExpertSignup(View):
    def get(self,request):
        return render(request,'expertsignup.html')

    def post(self, request):
         data=request.POST
         user=request.user
         fullname = data["fullname"]
         # address = data["address"]
         gender = data["gender"]
         company = data["company"]
         post = data["post"]
         experience = data["exp"]
         user.expert_status=True
         s1=ExpertRegisterTable(user_id=user,full_name=fullname,company=company,gender=gender,post=post,experience=experience)
         # r1=Myuser(address=address)
         s1.save()
         user.save()
         # r1.save()

         return redirect('/login/')



class CompanySignup(View):
    def get(self,request):
        return render(request,'companysignup.html')

    def post(self,request):
         data=request.POST
         company = data["cname"]
         address = data["address"]
         position = data["position"]
         cuser = data["cusername"]
         cpass = data["cpassword"]
         state = data["state"]
         city = data["city"]
         ainfo = data["ainfo"]
         phone = data["phonenbr"]
         email1=data["email1"]
         u3=Myuser.objects.create_user(username=cuser,password=cpass,email=email1,phone_no=phone,address=address,is_staff=True)
         u3.save()

         c1=CompanyRegisterTable(user_id=u3,company_name=company,category=position,state=state,city=city,additional_information=ainfo)
         c1.save()
         return redirect('/login/')

class CompanyHome(View):
    def get(self,request):

        # user=request.user
        # cmp=CompanyRegisterTable.objects.get(user_id=user)
        # jobs=Company_Jobs.objects.filter(company_id=cmp)
        return render(request, 'cmphome.html')




class PostJob(View):
    def get(self,request):
        return render(request,'postjob.html')
    def post(self,request):
        data=request.POST
        user=request.user
        companyobj=CompanyRegisterTable.objects.get(user_id=user)
        jobname = data["job_name"]
        jobd= data["job_det"]
        exp = data["exp"]
        qual=data["qual"]
        salary= data["salary"]
        jobs=Company_Jobs(company_id=companyobj,job_name=jobname,job_details=jobd, qualification=qual,experience=exp,salry=salary)
        jobs.save()
        return redirect('/viewappl/')


class ViewApplicants(View):
    def get(self, request):
        user = request.user
        cmp = CompanyRegisterTable.objects.get(user_id=user)
        jobs = Company_Jobs.objects.filter(company_id=cmp)
        return render(request, 'viewapplicants.html', {'jobs': jobs})
class ViewUserinfo(View):
    def get(self, request,id):
        job=Company_Jobs.objects.get(id=id)
        ap=Applied_jobs.objects.filter(applied_job=job)
        # return HttpResponse(ap)
        return render(request, 'applieduserinfo.html',{ 'ap':ap})

      # pass



class ViewAcinfo(View):
    def get(self, request,id):
        apjob=Applied_jobs.objects.get(id=id)
        apjob.status=1
        apjob.save()
        rmail=apjob.applied_user.email
        sub=apjob.applied_job.job_name
        send_mail(
            'invitation letter',
            'congratulation to be part of our team'+" "+sub,
            'zaidanwar962@gmail.com',
            [rmail],
            )
        return redirect('/cmphome/')




class ViewRjinfo(View):
    def get(self, request,id):
        apjob = Applied_jobs.objects.get(id=id)
        apjob.status = 2
        apjob.save()
        rmail = apjob.applied_user.email
        sub = apjob.applied_job.job_name
        send_mail(
            'your application rejected',
            'feedback from the company' + " " + sub,
            'zaidanwar962@gmail.com',
            [rmail],
        )
        return redirect('/cmphome/')

class UserLogin(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        data=request.POST
        us=data["username"]
        pas=data["pass"]
        user=authenticate(request,username=us,password=pas)
        if user is not None:
            login(request,user)
            if user.is_staff==True:
                return redirect('/cmphome/')
            else:

                return redirect('/userhome/')
        else:
            return HttpResponse("invalid user")

class UserHome(View):
    def get(self,request):
        # return render(request,'userhome.html')
        job = Company_Jobs.objects.all()
        # u=request.user
        # company=CompanyRegisterTable.objects.get(user_id=request.user)
        #
        # Company_Jobs.objects.filter(company_id=company)
        return render(request, 'userhome.html', {'job': job})

        # job=Company_Jobs.objects.all()
        # return render(request,'userhome.html' ,{'job':job})

class AplliedJob(View,):
    def get(self,request,id):

        user=request.user
        job_info=Company_Jobs.objects.get(id=id)

        # userobj = Myuser.objects.get(user_id=user)
        # cmpobj = CompanyRegisterTable.objects.get(user_id=cmp_id)
        obj=Applied_jobs(applied_user=user,applied_job=job_info,applied_date=date.today())

        obj.save()
        return redirect('/userhome/')
class AplliedJoblist(View,):
    def get(self,request):
        user=request.user
        obj=Applied_jobs.objects.filter(applied_user=user)
        # return HttpResponse(obj.applied_user.username)

        return render(request,'appliedjoblist.html' ,{'obj':obj})


class UserProfile(View):
            def get(self, request):
                user=request.user
                if user.expert_status==False:
                    obj1=FresherRegisterTable.objects.get(fresher_id=user)
                    return render(request,'profile.html' ,{'obj':obj1})
                else:
                    obj2 = ExpertRegisterTable.objects.get(user_id=user)

                    return render(request, 'eprofile.html', {'obj': obj2})


class EditProfile(View):


    def get(self, request):
        user = request.user
        if user.expert_status==False:
            obj1 = FresherRegisterTable.objects.get(fresher_id=user)
            return render(request, 'editprofile.html', {'obj': obj1})
        else:
            obj2 = ExpertRegisterTable.objects.get(user_id=user)
            return render(request, 'eeditprofile.html', {'obj': obj2})

    def post(self,request):
        data=request.POST
        user=request.user
        if user.expert_status==False:
            obj1 = FresherRegisterTable.objects.get(fresher_id=user)
            user.username=data['username']
            user.email=data['email']
            user.Phone_no=data['phone']

            user.address=data['address']
            user.save()
            obj1.full_name=data['fullname']
            obj1.city=data['city']
            obj1.state=data['state']
            obj1.college=data['college']
            obj1.degree=data['degree']
            obj1.specialization = data['spec']
            obj1.save()
            return redirect('/userhome/')
        else:
            obj2=ExpertRegisterTable.objects.get(user_id=user)
            user.username = data['username']

            user.email = data['email']
            user.Phone_no = data['phone']

            user.address = data['address']
            user.save()
            obj2.full_name = data['fullname']
            obj2.company = data['company']
            obj2.post = data['post']
            obj2.experience = data['exp']
            obj2.save()
            return redirect('/userhome/')







        # return HttpResponse(user)



