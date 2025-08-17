from django.shortcuts import render,redirect
from user.models import *
from django.core.files.storage import FileSystemStorage
import datetime

# Create your views here.

def teacherdash(request):
    try:
        if request.session['teacher']!=None:
            teacherid=request.session['teacher']
            teacher=Teacher.objects.get(email=teacherid)
            stu_count=Student.objects.all().count()
            sub_count=Subjects.objects.all().count()
            return render(request,"teacherdash.html",locals())
        
    except:
        return redirect('login')    
    
def teacherlogout(request):
    try:
        if request.session['teacher']!=None:
            del request.session['teacher']
            return redirect('login')
    except:
        return redirect('login')   
      
def teachersubjects(request):
    #try:
        if request.session['teacher']!=None:
            teacherid=request.session['teacher']
            teacher=Teacher.objects.get(email=teacherid)
            sub=Subjects.objects.filter(teacherid=teacher.id)
            return render(request,"teachersubjects.html",locals())
        
    #except:
        return redirect('login')   

def teacherattend(request):
    try:
        if request.session['teacher']!=None:
            teacherid=request.session['teacher']
            teacher=Teacher.objects.get(email=teacherid)
            return render(request,"teacherattend.html",locals())
        
    except:
        return redirect('login')      

def teacherprofile(request):
    try:
        if request.session['teacher']!=None:
            teacherid=request.session['teacher']
            t=Teacher.objects.get(email=teacherid)
            if request.method=="POST":
               pic=request.FILES['pic']
               fs=FileSystemStorage()
               filename=fs.save(pic.name,pic)
               t.pic=filename
               t.save()
               return redirect('teacherapp:teacherprofile') 
            return render(request,'teacherprofile.html',{'t':t})
    except:
        return redirect('login')
          
def teacherattend(request):
    # try:
        if request.session['teacher']!=None:
            teacherid=request.session['teacher']
            teacher=Teacher.objects.get(email=teacherid)
            students=Student.objects.filter(sclass=teacher.tclass)
            att=StudentAttendance.objects.filter(sclass=teacher.tclass)
            if request.method=="POST":
                studentid=request.POST['studentid']
                studentname=request.POST['studentname']
                sclass=request.POST['sclass']
                d=datetime.datetime.today()
                date=d.strftime("%Y-%m-%d")
                status=request.POST['status']
                stu=StudentAttendance(studentid=studentid,sclass=sclass,date=date,status=status,studentname=studentname,)
                stu.save()
                return redirect('teacherapp:teacherattend')
            return render(request,"teacherattend.html",locals())
    # except:
        # return redirect('login')    