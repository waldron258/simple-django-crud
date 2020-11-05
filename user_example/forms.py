from django.forms import ModelForm
from .models import Car

class CarRegisterForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class CarUpdateForm(ModelForm):
    class Meta:
        model = Car
        fields = ['plate', 'carModel', 'year']
