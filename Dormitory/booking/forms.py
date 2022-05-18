from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['phone', 'gender', 'course', 'faculty']


class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'floor', 'block']


class CheckRoomForm(forms.Form):
    COURSE = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
    ]
    FACULTY = [
        ('Faculty of Law and Social Sciences', 'Faculty of Law and Social Sciences'),
        ('Faculty of Education and Humanities Sciences', 'Faculty of Education and Humanities Sciences'),
        ('Faculty of Engineering and Natural Sciences', 'Faculty of Engineering and Natural Sciences'),
        ('Business school', 'Business school')
    ]
    GENDER = [
        ('m', 'Male'),
        ('f', 'Female')
    ]
    gender = forms.models.ChoiceField(choices=GENDER, required=True)
    course = forms.models.ChoiceField(choices=COURSE, required=True)
    faculty = forms.models.ChoiceField(choices=FACULTY, required=True)


class BookForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
