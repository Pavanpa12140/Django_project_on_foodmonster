from django import forms
from .models import Vender

class venderForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Vender
        fields = ('vender_name','vender_liciense','password','confirm_password')