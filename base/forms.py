from django.forms import ModelForm
from .models import Room, User
from django.contrib.auth.forms import UserCreationForm

class myusercreationform(UserCreationForm):
    class Meta:
        model = User
        fields = ("name", "username", "email", "password1", "password2")

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ("topic","name","description") 
        labels = {
            "topic": "temat",
            "name": "nazwa",
            "description": "opis",
            }
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("avatar","name", "username", "email", "bio",)
        labels = {
            "username": "Nazwa użytkownika",
            "email": "E-mail",
        }