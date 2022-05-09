from dataclasses import field
import email
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    firstname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone = forms.NumberInput()
    class Meta:
        model =User
        fields = ['username','firstname', 'lastname', 'email', 'password1', 'password2',]