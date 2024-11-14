from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Account


class RegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email', 'username', 'about', 'avatar']

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.replace(' ', '').isalnum():
            raise ValidationError(
                "Имя пользователя может содержать только буквы, цифры и пробелы.")
        return username
