from django.urls import path
from taskmanagement import views


urlpatterns = [
    path('',views.home,name='home'),
    path('registrationform',views.registrationform,name='registrationform'),
    path('register',views.register,name='register'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('usertask',views.usertask,name='usertask'),
    path('viewtask',views.viewtask,name='viewtask'),
    path('createtask',views.createtask,name='createtask'),
    path('update/<int:pk>',views.update,name='update'),
    path('updatetask/<int:pk>',views.updatetask,name='updatetask'),
    path('removetask/<int:pk>',views.removetask,name='removetask'),
    path('logout',views.logout,name='logout'),


    
]
