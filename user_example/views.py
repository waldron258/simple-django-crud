from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Car
from django.http import JsonResponse 
from django.views import View
from django.forms.models import model_to_dict
from .forms import CarRegisterForm, CarUpdateForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from django.contrib.auth import logout as django_logout


# Index view
@login_required(login_url='login')
def index(request):
    return render (request, 'C:/Users/Waldron/Documents/BRAIN/Django/login_example/login_example/templates/registration/index.html')


# Logout view
def logout(request):
    django_logout(request)
    return  redirect('/login')


# Register an user view
@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            group = Group.objects.get(name='SLAVE')
            
            group.user_set.add(user)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)


# Register a car view
@login_required(login_url='login')
@allowed_users(allowed_roles=['MASTER'])
def createCar(request):
    if request.method == 'POST':
        form = CarRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CarRegisterForm()
        
    context = {'form': form}
    return render(request, 'registration/car_register.html', context)


# Update a car view
@login_required(login_url='login')
@allowed_users(allowed_roles=['MASTER'])
def updateCar(request, pk):
    car = Car.objects.get(id=pk)
    form = CarUpdateForm(instance=car)
    if request.method == 'POST':
        form = CarUpdateForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('/car-list')
    return render(request, 'C:/Users/Waldron/Documents/BRAIN/Django/login_example/user_example/templates/user_example/car_update.html', {'car': car})
   

# Car list
class Cars(ListView): 
    model = Car
    @login_required(login_url='login')
    def getCarList(self):
        return Car.objects.all()

