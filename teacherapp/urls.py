from django.urls import path
from . import views

urlpatterns=[
    path('teacherapp/',views.teacherdash,name="teacherdash"),
    path('teacherlogout/',views.teacherlogout,name="teacherlogout"),
    path('teachersubjects/',views.teachersubjects,name="teachersubjects"),
    path('teacherattend/',views.teacherattend,name="teacherattend"),
    path('teacherproflie/',views.teacherprofile,name="teacherprofile"),
]