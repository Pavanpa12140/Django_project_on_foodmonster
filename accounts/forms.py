from django import forms
from .models import User
from django.core.exceptions import ValidationError

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name','last_name','email','password','confirm_password','username','role')

    def clean(self):
        all_cleaned_data = super(userForm,self).clean()
        pswd = all_cleaned_data.get('password')
        con_pswd = all_cleaned_data.get('confirm_password')

        if pswd != con_pswd:
            raise forms.ValidationError('Password not matched')