from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect, get_object_or_404
from .forms import  OrderingCreationForm
from .models import Ordering, Course



# Create your views here.

def index(request):
    return render(request,'index.html')

def loginn(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('main')
        else:
            messages.info(request, "username or password are incorrect")
            return redirect('login')
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email_id']
        password=request.POST['password']
        cpaswd=request.POST['cpassword']

        if password==cpaswd:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect('signup')

            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save()
                return redirect('login')
            print("user created")

        else:
            messages.info(request,"password not matching")
            return redirect('signup')
        return redirect('/')
    return render(request,'register.html')

def logged(request):
     return render(request,"main.html")
def logout(request):
    auth.logout(request)
    return redirect('/')


def create_view(request):
    form = OrderingCreationForm()
    if request.method == 'POST':
        form = OrderingCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Order Confirmed')
            return redirect('add')
    return render(request, 'order.html', {'form': form})


def update_view(request, pk):
    ordering = get_object_or_404(Ordering, pk=pk)
    form = OrderingCreationForm(instance=ordering)
    if request.method == 'POST':
        form = OrderingCreationForm(request.POST, instance=ordering)
        if form.is_valid():
            form.save()
            return redirect('add', pk=pk)
    return render(request, 'order.html', {'form': form})


# AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'course_dropdown_list_options.html', {'courses': courses})


