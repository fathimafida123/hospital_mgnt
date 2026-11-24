from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class Registration(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=["username","email"]