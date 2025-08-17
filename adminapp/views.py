from django.shortcuts import render,reverse,redirect
import datetime
from user.models import *
# Create your views here.

def adminhome(request):
    try:
        if request.session['username']!=None:
            stu_count=Student.objects.all().count()
            t_count=Teacher.objects.all().count()
            c_count=Class.objects.all().count()
            return render(request,'adminhome.html',locals())
    except:
        return redirect('login')

def teacher(request):
    try:
        if request.session['username']!=None:
            if request.method=="POST":
                name=request.POST['name']
                number=request.POST['number']
                email=request.POST['email']
                qua=request.POST['qua']
                exp=request.POST['exp']
                tsalary=request.POST['tsalary']
                tclass=request.POST['tclass']
                address=request.POST['address']
                password=request.POST['password']
                created=datetime.datetime.today()
                teacher=Teacher(name=name,phone=number,email=email,qualification=qua,tsalary=tsalary,tclass=tclass,experience=exp,created=created,address=address,)
                teacher.save()
                t=Teacher.objects.all()
                cl=Class.objects.all()
                log=LoginUser(username=email,password=password,userType="teacher")
                log.save()
                return render(request,'teacher.html',{'msg':"Teacher is Added",'t':t,'cl':cl})
            t=Teacher.objects.all()
            cl=Class.objects.all()
            return render(request,'teacher.html',{'t':t,'cl':cl})
        
    except:
        return redirect('login')    
    
  
    

def student(request):
    try:
        if request.session['username']!=None:
            stu=Student.objects.all()
            if request.method=="POST":
                name=request.POST['name']
                number=request.POST['number']
                email=request.POST['email']
                password=request.POST['password']
                fname=request.POST['fname']
                fnumber=request.POST['fnumber']
                sclass=request.POST['sclass']
                sfees=request.POST['sfees']
                balance=request.POST['balance']
                address=request.POST['address']
                dob=request.POST['dob']
                stu=Student(name=name,mobile=number,email=email,fnumber=fnumber,fname=fname,sclass=sclass,sfee=sfees,balance=balance,address=address,dob=dob)
                stu.save()
                log=LoginUser(username=email,password=password,userType="student")
                log.save()
                msg="STUDENT IS ADDED SUCCESFULLY"
                stu=Student.objects.all()
                cl=Class.objects.all()
                return render(request,'student.html',{'msg':msg,'stu':stu,'cl':cl})
            stu=Student.objects.all()
            cl=Class.objects.all()
            return render(request,'student.html',{'stu':stu , 'cl':cl})
                     
    except:
            return redirect('login')
    

def attendance(request):
    try:
        if request.session['username']!=None:
            attend=StudentAttendance.objects.all()
            return render(request,'attendance.html',{'attend':attend})
    except:
        return redirect('login')
    

def classes(request):
    try:
        if request.session['username']!=None:
            c=Class.objects.all()
            if request.method=="POST":
                name=request.POST['name']
                roomno=request.POST['roomno']
                seats=request.POST['seats']
                c=Class(name=name,roomno=roomno,seats=seats)
                c.save()
                return redirect('adminapp:classes')
            return render(request,'classes.html',locals())
    except:
        return redirect('login')
    

def logout(request):
    try:
        if request.session['username']!=None:
            del request.session['username']
            return redirect('login')
    except:
        return redirect('login')     

def delteacher(request,id):
    try:
        if request.session['username']!=None:
            Teacher.objects.get(id=id).delete()
            return redirect('adminapp:teacher')
    except:
        return redirect('login')
    
    
def delstudent(request,id):
    try:
        if request.session['username']!=None:
            Student.objects.get(id=id).delete()
            return redirect('adminapp:student')
    except:
        return redirect('login')   
    
def delsubject(request,id):
    #try:
        if request.session['username']!=None:
            Subjects.objects.get(id=id).delete()
            return redirect('adminapp:subject')
    #except:
        #return redirect('login')    
    
def edit(request,id):
    try:
        if request.session['username']!=None:
            stu=Student.objects.get(id=id)
            cl=Class.objects.all()
            if request.method=="POST":
                name=request.POST['name']
                fname=request.POST['fname']
                number=request.POST['number']
                fnumber=request.POST['fnumber']
                dob=request.POST['dob']
                sfees=request.POST['sfees']
                sclass=request.POST['sclass']
                balance=request.POST['balance']
                address=request.POST['address']
                Student.objects.filter(id=id).update(name=name,fname=fname,mobile=number,sfees=sfees,sclass=sclass,dob=dob,fnumber=fnumber,balance=balance,address=address)
                return redirect('adminapp:student')
            return render(request,'edit.html',{'stu':stu,'cl':cl})
    except:
        return redirect('login')        
    
def tedit(request,id):
    try:
        if request.session['username']!=None:
            t=Teacher.objects.get(id=id)
            if request.method=="POST":
                name=request.POST['name']
                email=request.POST['email']
                number=request.POST['number']
                qua=request.POST['qua']
                exp=request.POST['exp']
                tsalary=request.POST['tsalary']
                tclass=request.POST['tclass']
                created=request.POST['created']
                address=request.POST['address']
                Teacher.objects.filter(id=id).update(name=name,phone=number,email=email,qualification=qua,tsalary=tsalary,tclass=tclass,experience=exp,created=created,address=address,)
                return redirect('adminapp:teacher')
            return render(request,'edit.html',{'t':t})
    except:
        return redirect('login')   
    
def Class_Edit(request,id):
    #try:
        if request.session['username']!=None:
            c=Class.objects.get(id=id)
            if request.method=="POST":
                name=request.POST['name']
                roomno=request.POST['roomno']
                seats=request.POST['seats']
                Class.objects.filter(id=id).update(name=name,roomno=roomno,seats=seats)
                return redirect('adminapp:classes')
            return render(request,'classes.html',locals())
    #except:
        return redirect('login')    
    
def subject(request):
    #try:
        if request.session['username']!=None:
            cl=Class.objects.all()
            sub=Subjects.objects.all()
            teacher=Teacher.objects.all()
            if request.method=="POST":
                name=request.POST['name']
                classid=request.POST['classid']
                teacherid=request.POST['teacherid']
                book=request.POST['book']
                s=Subjects(name=name,classid=classid,teacherid=teacherid,book=book)
                s.save()
                return redirect('adminapp:subject')

            return render(request,'subject.html',locals())
    #except:
        #return redirect('login')
    
def index(request):
    try:
        if request.session['username']!=None:
            return redirect('adminapp:index')
    except:
        return redirect('login')    
    
def viewenqiry(request):
    try:
        if request.session['username']!=None:
            enq=Enquiry.objects.all()
            return render(request,'viewenqiry.html',locals())
    except:
        return redirect('login')    

def admincp(request):
    try:
        if request.session['username']!=None:
            adminid=request.session['username']
            if request.method=="POST":
                oldpassword=request.POST['oldpassword']
                newpassword=request.POST['newpassword']
                cpassword=request.POST['cpassword']
                try:
                    obj=LoginUser.objects.get(username=adminid,password=oldpassword)
                    if newpassword!=cpassword:
                        msg="Enter same password"
                        return render(request,'admincp.html',locals())
                    elif oldpassword==obj.password:
                        LoginUser.objects.filter(username=adminid,password=oldpassword).update(password=newpassword)
                        return redirect('adminapp:logout')
                except:
                    return render(request,'admincp.html',{'msg':"Inavalid Old Password"})

            return render(request,'admincp.html',locals())
    except:
        return redirect('login')     