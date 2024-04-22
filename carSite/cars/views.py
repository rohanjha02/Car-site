from django.shortcuts import render
from .models import *
from carSite.settings import BASE_DIR
# Create your views here.

def index(request):
    # cars_data.objects.all().delete() #To Delete the data
    cars = cars_data.objects.all()
    return render(request, 'index.html', {'cars':cars, 'BASE_DIR':BASE_DIR})


def admin1(request):
    if request.method == 'POST':
        car = cars_data()
        car.car_Name = request.POST.get("car_name", False)
        car.car_Price = request.POST.get("car_price", False)
        car.Car_Model = request.POST.get("car_model", False)
        car.car_Photo = request.FILES.get("car_photo", False)
        car.save()

    
    return render(request, 'upload.html')