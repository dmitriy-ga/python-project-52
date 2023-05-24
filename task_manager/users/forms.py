from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, \
    UsernameField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django import forms


user_model = get_user_model()


class SignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = user_model
        fields = ('username', 'first_name', 'last_name')


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={"autofocus": True, "placeholder": _("Username")}))

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          "placeholder": _("Password")}),
    )


class UpdateForm(SignupForm):
    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username
