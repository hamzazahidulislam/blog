from django import forms
from main_blog.models import *


class UserLogin(forms.Form):
    user_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
