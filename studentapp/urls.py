from django.urls import path
from .import views

urlpatterns=[
path('studentapp/',views.studentdash,name="studentdash"),
path('studentprofile/',views.studentprofile,name="studentprofile"),
path('studentlogout/',views.studentlogout,name="studentlogout"),
path('stu_subject/',views.stu_subject,name="stu_subject"),
path('stu_attendance/',views.stu_attendance,name="stu_attendance"),
]