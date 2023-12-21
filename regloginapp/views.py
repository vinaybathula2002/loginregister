from django.shortcuts import render,redirect
from django .views import View
from django .http import HttpResponse
from regloginapp.models import regmodel
class home(View):
    def get(self,request):
        return render(request,'home.html')
class reginput(View):
    def get(self,request):
        """v=regmodel.objects.all()
        print(v)"""
        return render(request,'reginput.html')

class reg(View):
    def get(self,request):
        fn= request.GET['fn'],
        ln=request.GET['ln'],
        us= request.GET['us'],
        password= request.GET['password'],
        cpassword= request.GET['cpassword'],
        emailid= request.GET['emailid'],
        mobno= request.GET['mobno']
        c=regmodel(First_name=fn,Last_name=ln,User_name=us,Password=password,Cpassword=cpassword,Email_id=emailid,Mobno=mobno)
        c.save()
        return HttpResponse('success')
class logininput(View):
    def get(self,request):
        return render(request,'logininput.html')
class login(View):
    def post(self,request):
        if request.method=='POST':
            user=request.POST['us']
            password=request.POST['password']
            print(password)
            log=regmodel.objects.filter(User_name=user,Password=password)
            print(log)
            if log:
                return HttpResponse('login success')
            else:
                return redirect("logininput")