from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import TextInput
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'placeholder': 'Введите email'}),
    )
    error_messages = {
        "password_mismatch": _("Пароли должны совпадать!"),
    }
    password1 = forms.CharField(
        label=_("Введите пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': 'Введите пароль'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Ещё раз"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': 'Ещё раз'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Введите логин'})
        }


