from . models import UserRegistration,Admin_panel
from django import forms

class AdminForm(forms.ModelForm):
        class Meta:
                model = Admin_panel
                fields =['username','password',"email"]
                widgets = {'password':forms.PasswordInput}


class USerForm(forms.ModelForm):
        class Meta:
                model = UserRegistration
                fields = ['name','email_id','qualification','address']

class UpdateForm(forms.ModelForm):
        class Meta:
                model = UserRegistration
                fields = "__all__"

class UserSearchForm(forms.ModelForm):
        class Meta:
                model =UserRegistration
                fields = ['name','email_id']