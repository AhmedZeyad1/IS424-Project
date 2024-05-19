from django import forms
from .models import User , book


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'user_email', 'user_phoneNumber' , "user_password"]

class UserLogin(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_phoneNumber' , "user_password"]        


class AddBook(forms.ModelForm):
    class Meta:
        model= book
        fields =["title","publicationDate","ISBN","bookGenre","author"]         