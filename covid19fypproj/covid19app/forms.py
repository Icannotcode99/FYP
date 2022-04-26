from django import forms
from django.contrib.auth.models import User
from .models import User


# Create your forms here.

class LoginForm(forms.Form):
	username = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				"class": "form-control"
			}
		)
	)

	password = forms.CharField(
		widget = forms.PasswordInput(
			attrs = {
				"class": "form-control"
			}
		)
	)
	class Meta:
		model = User
		fields = ("username", "password", 'Is_medical', 'Is_expert')

