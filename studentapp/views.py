from django.shortcuts import render,redirect
from user.models import *
from django.core.files.storage import FileSystemStorage

# Create your views here.

def studentdash(request):
    try:
        if request.session['student']!=None:
            studentid=request.session['student']
            stu=Student.objects.get(email=studentid)
            sub_count=Subjects.objects.all().count()
            attend_count=StudentAttendance.objects.all().count()
            return render(request,'studentdash.html',{'stu':stu,'sub_count':sub_count})
    except:
        return redirect('login')

def studentprofile(request):
    try:
        if request.session['student']!=None:
            studentid=request.session['student']
            stu=Student.objects.get(email=studentid)
            if request.method=="POST":
               pic=request.FILES['pic']
               fs=FileSystemStorage()
               filename=fs.save(pic.name,pic)
               stu.pic=filename
               stu.save()
               return redirect('studentapp:studentprofile') 
            return render(request,'studentprofile.html',{'stu':stu})
    except:
        return redirect('login')
    
def studentlogout(request):
    try:
        if request.session['student']!=None:
            del request.session['student']
            return redirect('login')
    except:
        return redirect('login')  
       
def stu_subject(request):
    try:
        if request.session['student']!=None:
            studentid=request.session['student']
            stu=Student.objects.get(email=studentid)
            sub=Subjects.objects.filter(classid=stu.sclass) 
            return render(request,'stu_subject.html',{'stu':stu,'sub':sub})
    except:
        return redirect('login')
    
def stu_attendance(request):
    try:
        if request.session['student']!=None:
            studentid=request.session['student']
            stu=Student.objects.get(email=studentid)
            att=StudentAttendance.objects.filter(studentid=stu.id)
            return render(request,'stu_attendance.html',{'stu':stu,'att':att})
    except:
        return redirect('login')       

