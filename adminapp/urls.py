from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('adminhome',views.adminhome,name="adminhome"),
   path('index',views.index,name="index"),
   path('teacher',views.teacher,name="teacher"),
   path('student',views.student,name="student"),
   path('attendance',views.attendance,name="attendance"),
   path('classes',views.classes,name="classes"),
   path('logout',views.logout,name="logout"),
   path('delteacher/<id>',views.delteacher,name="delteacher"),
   path('delstudent/<id>',views.delstudent,name="delstudent"),
   path('delsubject/<id>',views.delsubject,name="delsubject"),
   path('edit/<id>',views.edit,name="edit"),
   path('tedit/<id>',views.tedit,name="tedit"),
   path('Class_Edit/<id>',views.Class_Edit,name="Class_Edit"),
   path('subject',views.subject,name="subject"),
   path('viewenquiry',views.viewenqiry,name="viewenqiry"),
   path('admincp',views.admincp,name="admincp"),

]