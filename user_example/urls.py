from django.urls import path, include
from . import views
from user_example.views import Cars
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('create-car/', views.createCar , name='create_cars'),
    path('update-car/<str:pk>/', views.updateCar, name="update_cars"),
    path('car-list/', login_required(views.Cars.as_view(),'login')),
    path('logout/', views.logout, name='logout'),
]