
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate , logout#add this
from django.contrib.auth.forms import AuthenticationForm #add this


# Create your views here.

    
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Automatically log in the user after registration
            messages.success(request,f"user : {user.username} saved successfully...!")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to home page after successful registration
        messages.error(request, "Unsuccessful Signup, Data is Invalid....!")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'signup_form': form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username= user_name, password= password)
            if user:
                login(request,user)
                messages.success(request, "Logged in successfully...!")
                return redirect("homepage")
        else:
            messages.error(request,"Invalid credentials.!")
        # return redirect("home_page")
    else:
        return render(request,"login.html",{'login_form':AuthenticationForm()})
# def user_login(request):
#     return render(request,'register.html')

    
def user_logout(request):
    logout(request)
    return redirect("user_signin")
