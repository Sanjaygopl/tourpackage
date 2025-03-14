from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import Explores,models
from .models import Venreg
from .models import Venlog
from .models import Usereg
from .models import Uselog


class ExploreForm(forms.ModelForm):
  class Meta:
        model=Explores
        fields = ['title', 'destination', 'image', 'duration', 'price','expiry']
        widgets = {'expiry' : forms.DateInput(format='%d/%m/%Y')}
class VregistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields =['username','email','password1','password2']
class VloginForm(forms.ModelForm):
    class Meta:
        model=Venlog
        fields =['username','password']
class UregistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields =['username','email','password1', 'password2']
class UloginForm(forms.ModelForm):
    class Meta:
        model=Uselog
        fields=['username','password']

