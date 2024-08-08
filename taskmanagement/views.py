from django.shortcuts import render,redirect
from taskmanagement.models import Task
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'taskmanagement.html')
def registrationform(request):
    return render(request,'registrationform.html')
def register(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pswrd']
        cpassword=request.POST['cpswrd']
        if password==cpassword :
            if User.objects.filter(username=email).exists():
                messages.info(request,'USERNAME ALREADY EXISTS')
                return redirect('registrationform')
            else:
                user=User.objects.create_user(first_name=firstname,
                                              last_name=lastname,
                                              email=email,
                                              username=email,
                                              password=password)
                user.save()
                return redirect('loginpage')
        else:
            messages.info(request,'PASSWORD MISMATCH')
            return redirect('registrationform')

def loginpage(request):
    return render(request,'loginpage.html')

def loginuser(request):
    if request.method=='POST':
        username=request.POST.get('email')
        password=request.POST.get('pswrd')   
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            admin = User.objects.get(username=username)
            if admin.is_staff:
                login(request,user)
                return redirect('adminpage')
            else:
                login(request,user)
                auth.login(request,user)
                return redirect('usertask')
        else:
            return redirect('loginpage')
    else:
        return redirect('loginpage')

def adminpage(request):
    return render(request,'adminpage.html')
@login_required(login_url='loginpage')
def usertask(request):
    return render(request,'taskcreate.html')
@login_required(login_url='loginpage')
def createtask(request):
    if request.method=='POST':
        title=request.POST['task']
        description=request.POST['desc']
        complete=request.POST['completed']
        task=Task(title=title,description=description,completed=complete)
        task.save()
        messages.info(request,'Task created successfully')
        return redirect('loginpage')
@login_required(login_url='loginpage')
def update(request,pk):
    task=Task.objects.get(id=pk)
    return render(request,'taskupdate.html',{'task':task})
@login_required(login_url='loginpage')
def updatetask(request,pk):
     task=Task.objects.get(id=pk)
     if request.method=='POST':
      task.title=request.POST['task']
      task.description=request.POST['desc']
      task.completed=request.POST['completed']
      task.save()
      return redirect('viewtask')
     return render(request, 'taskupdate.html', {'task': task})
@login_required(login_url='loginpage')
def removetask(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect('viewtask')
@login_required(login_url='loginpage')
def viewtask(request):
    query = request.GET.get('q', '')
    if query:
        tasks = Task.objects.filter(title__icontains=query) | Task.objects.filter(description__icontains=query)
        tasks_found = tasks.exists()  # Check if any tasks were found
    else:
        tasks = Task.objects.all()
        tasks_found = tasks.exists()  # Check if any tasks were found
    task=Task.objects.all()
    return render(request,'viewtask.html',{'task':task,'tasks_found':tasks_found})
def logout(request):
    auth.logout(request)
    return redirect('home')