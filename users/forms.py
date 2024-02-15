# users/forms.py
# imported CustomUser model via get_user_model that define in settings.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# class creation users form
class CustomUserCreationForm(UserCreationForm):
    #displaying the fields email, username and password is inclu default
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',) 

# class change users form
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)