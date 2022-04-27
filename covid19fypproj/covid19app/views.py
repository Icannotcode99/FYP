from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth  import  authenticate , login 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import expertdata #add this
from .forms import LoginForm
from django.core import serializers


# Create your views here.
def home(request):
    return render(request, "covid19app/home.html")


def login_page(request):
    #  if request.method == "POST":
    #     #  username=request.POST['username']
    #     #  password=request.POST['password']
    #      username = request.POST.get('username')
    #      password = request.POST.get('password')
    #      form = NewUserForm(username = username , password = password)
    #      print(username)
    #      user = authenticate(request, username=username, password=password)
    #      if user is not None:
    #         login(request, user)
    #         print('logged in ')
    #         return redirect("/home")
    #      else:
    #         messages.success(request, "Login failed, please try again.")
    #         return redirect("/home")
    #  else:
    #      return render(request, 'home/login.html')
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_Medical:
                login(request, user)
                return redirect("medical")
            elif user is not None and user.is_Expert:
                login(request, user)
                return redirect("IT")
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'covid19app/login.html', {'form':form, 'msg':msg})

    #  if request.method == "POST":
    #      form = AuthenticationForm(request, data=request.POST)
    #      if form.is_valid():
    #          username = form.cleaned_data.get('username')
    #          password = form.cleaned_data.get('password')
    #          user = authenticate(username=username, password=password)
    #          if user is not None:
    #              login(request, user)
    #              messages.info(request, f"You are now logged in as {username}.")
    #              return redirect("home")
    #          else:
    #              messages.error(request,"Invalid username or password.")
    #      else:
    #          messages.error(request,"Invalid username or password.")
    #  form = AuthenticationForm()
    #  return render(request=request, template_name="covid19app/login.html")
@login_required

def logout(request):
    pass


def medical(request):
    return render(request, 'covid19app/medical.html')


def IT(request):
    return render(request, 'covid19app/IT.html')


def displayData(request):
    data = serializers.serialize("python", expertdata.objects.all())
    context = {
        'data':data,
    }
    return render(request, 'medical.html', context)

