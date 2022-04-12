from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import TextInput, EmailInput, CheckboxInput, Textarea, Select, FileInput

from main.models import User, Category, Ad


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'city', 'birthday', 'open_to_work', 'photo',
                  'about']
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Nume utilizator', 'class': 'form-control'}),
            'first_name': TextInput(attrs={'placeholder': 'Ex: Adi', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Ex: Baciu', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'adi.baciu@yahoo.com', 'class': 'form-control'}),
            'phone': TextInput(attrs={'placeholder': 'Numărul de telefon', 'class': 'form-control'}),
            'city': TextInput(attrs={'placeholder': 'Orașul', 'class': 'form-control'}),
            'birthday': TextInput(
                attrs={'placeholder': 'Data nasterii', 'class': 'form-control', 'type': 'date'}),
            'about': Textarea(
                attrs={'placeholder': 'Un rezumat despre dumneavoastră', 'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter password confirmation'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'active']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter your name', 'class': 'form-control'}),
        }


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['name', 'location', 'description', 'job_type', 'contract_type', 'education', 'local_or_distance',
                  'experience',
                  'salary', 'salary_type', 'category', 'image', 'active','phone']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter your name', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter your description', 'class': 'form-control'}),
            'salary': TextInput(attrs={'placeholder': 'Please enter your price', 'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'placeholder': 'Numărul de telefon', 'class': 'form-control'}),

        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'city', 'birthday', 'open_to_work', 'photo',
                  'about']
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Nume utilizator', 'class': 'form-control'}),
            'first_name': TextInput(attrs={'placeholder': 'Ex: Adi', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Ex: Baciu', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'adi.baciu@yahoo.com', 'class': 'form-control'}),
            'phone': TextInput(attrs={'placeholder': 'Numărul de telefon', 'class': 'form-control'}),
            'city': TextInput(attrs={'placeholder': 'Orașul', 'class': 'form-control'}),
            'birthday': TextInput(
                attrs={'placeholder': 'Data nasterii', 'class': 'form-control', 'type': 'date'}),
            'about': Textarea(
                attrs={'placeholder': 'Un rezumat despre dumneavoastră', 'class': 'form-control'}),
            'photo': FileInput()

        }
