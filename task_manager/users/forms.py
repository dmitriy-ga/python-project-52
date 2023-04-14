from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


user_model = get_user_model()


class SignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = user_model
        fields = ('username', 'first_name', 'last_name')


class LoginForm(AuthenticationForm):
    pass


class UpdateForm(SignupForm):
    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username
