from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import book 
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request,'home.html')
def shome(request):
    return render(request,'shome.html')
def books(request):
    book_dict={
        'books':book.objects.all()
               }
    return render(request,'sbooks.html',book_dict)

# def login(request):
#     if request.method =='GET':
#         return render(request,'login.html')
#     elif request.method == "POST":
#         username=request.POST['username']
#         password=request.POST['password']
        
        
        # check=logindata.objects.filter(username=username).exists()
        # if check:
        #         return render(request,'shome.html')
        # else:
        #     msg='invalid username or password'
        #     message_dict={'msg':msg}
        # return render(request,'login.html',message_dict)

 

# or  correct can use

        # login2=logindata.objects.all()
        # for i in login2:
        #     if username == i.username:

        #         login_name = i.name
        #         name_dict={'name':login_name}
        #         return render(request,'shome.html',name_dict)
        #     msg='invalid username or password'
        #     message_dict={'msg':msg}
        # return render(request,'login.html',message_dict)
   
# def newreg(request):
#     if request.method =='GET':
#         return render(request,'newreg.html')
#     elif request.method == "POST":
#         name=request.POST['name']
#         age=request.POST.get('age',None)
#         gender=request.POST.get('gender',None)
#         username=request.POST.get('username',"")
#         password=request.POST.get('password',"")
#         user1=newuser(name=name,age=age,gender=gender,username=username,password=password)
#         login1=logindata(name=name,username=username,password=password)
#         user1.save()
#         login1.save()
#         name_dict={'name':name}
#         return render(request,'shome.html',name_dict)
    

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            name_dict={
                'username':username
            }
            # return redirect('pg1')  # Redirect to home page or any other page
            return render(request,'shome.html',name_dict)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                name_dict={
                'username':username
                   }
                return render(request,'shome.html',name_dict)
                return redirect('pg1')  # Redirect to home any other page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})