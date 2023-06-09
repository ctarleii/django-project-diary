from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import Textarea
from django.forms import TextInput
from django.utils.translation import gettext_lazy as _

from school.models import News, Comments

User = get_user_model()


class UserCreationForm(UserCreationForm):

    # email
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'placeholder': 'Введите email'}),
    )

    # password
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
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    # first_name & last_name
    first_name = forms.CharField(
        label=_("Введите Имя"),
        strip=False,
        widget=forms.TextInput(attrs={"autocomplete": "first-name", 'placeholder': 'Введите Имя'}),
    )

    last_name = forms.CharField(
        label=_("Введите Фамилию"),
        strip=False,
        widget=forms.TextInput(attrs={"autocomplete": "last-name", 'placeholder': 'Введите Фамилию'}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "first_name", "last_name")
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Введите логин'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget = Textarea(attrs={'rows': 3, 'style': 'border-radius: 8px; width: 873px'})
