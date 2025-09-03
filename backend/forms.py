from django import forms
from .models import cityname

class inputform(forms.ModelForm):
 class Meta:
     model = cityname
     fields = '__all__'
