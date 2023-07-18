from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage, name="homepage"),
    path("viewachievement/",views.viewachievement, name='viewachievement'),
    path("viewachievementforstudent/",views.viewachievementforstudent, name='viewachievementforstudent'),
    path("registerstudents/",views.registerstudents,name='registerstudents'),
    path("loginstudents/",views.loginstudents,name='loginstudents'),
    path("registeradmin/",views.registeradmin,name='registeradmin'),
    path("loginadmin/",views.loginadmin,name='loginadmin'),
    path('create/level/', views.create_level, name='create_level'),
    path('create/category/', views.create_category, name='create_category'),
    path('create/achievment/', views.create_achievment, name='create_achievment'),
    path('deletedata_student/<str:student_id>/',views.deletedata_student,name='deletedata_student'),
    path('deleteachievement/<int:achievement_id>/', views.deleteachievement, name='deleteachievement'),
    path('admindata/',views.admindata,name='admindata'),
    path('searchpage/',views.searchpage,name='searchpage'),
    path('searchpageforstudent/',views.searchpageforstudent,name='searchpageforstudent'),
    path('updatestudent/<str:student_id>/', views.updatestudent, name='updatestudent'),
    path('updateadmin/<str:admin_id>/', views.updateadmin, name='updateadmin'),
    path('studentdata/', views.studentdata, name='studentdata'),
    path('studentdataforstudent/', views.studentdataforstudent, name='studentdataforstudent'),

]


