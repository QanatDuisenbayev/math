from django import forms
from django.contrib.auth import get_user_model
from mathapp.models import Elementary_math
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

User = get_user_model()

	
class LoginForm(forms.Form):

	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = 'Логин'
		self.fields['password'].label = 'Құпия сөз'

	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']

		if not User.objects.filter(username=username).exists():
			raise forms.ValidationError('login qate!')

		user = User.objects.get(username=username)
		if not user.check_password(password):
			raise forms.ValidationError('password qate!')


class RegistrationForm(forms.ModelForm):
	password_check = forms.CharField(widget=forms.PasswordInput)
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'password_check',
			'first_name',
			'last_name',
			'email',
		]

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = 'Логин'
		self.fields['username'].help_text = 'Маңызды бөлім 150 символдан аспайтын логин таңдаңыз'
		self.fields['password'].label = 'Құпия сөз'
		self.fields['password_check'].label = 'Құпия сөзді қайталаңыз'
		self.fields['first_name'].label = 'Атыңыз'
		self.fields['last_name'].label = 'Есіміңіз'
		self.fields['email'].label = 'email'


	def clean(self):
		password = self.cleaned_data['password']
		username = self.cleaned_data['username']
		password_check = self.cleaned_data['password_check']

		if len(password) < 5:
			raise forms.ValidationError('qupya soz ote kyska')

		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('basqa login tandanyz!')
		if password != password_check:
			raise forms.ValidationError('qupya soz saikes emes!')
	




class VideoForm(ModelForm):

	class Meta:
		model = Elementary_math
		fields = '__all__'



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
    	super(SignupForm, self).__init__(*args, **kwargs)
    	self.fields['username'].label = 'Логин'
    	self.fields['username'].help_text = 'Маңызды бөлім 150 символдан аспайтын логин таңдаңыз'
    	self.fields['password1'].label = 'Құпия сөз'
    	self.fields['password2'].label = 'Құпия сөзді қайталаңыз'
    	self.fields['email'].label = 'email'
