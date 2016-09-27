from django.contrib.auth.forms import UserCreationForm

from .models import MyUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = UserCreationForm.Meta.fields
