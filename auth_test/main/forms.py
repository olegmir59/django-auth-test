from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # Поля, которые будут отображаться в форме регистрации.
        # username — обязательно, email и phone_number добавлены.
        fields = ('username', 'email', 'phone_number')