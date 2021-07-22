from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Tasks

class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username',)

class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username',)


class TaskCreationForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = ('uid','task_title', 'task_description', 'task_pic',)
