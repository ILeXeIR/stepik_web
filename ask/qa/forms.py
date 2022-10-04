from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']
		labels = {'title': 'Title of your question', 'text': "What do you want to ask?"}

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['text']
		labels = {'text': 'Write your answer'}

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']

class RegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']