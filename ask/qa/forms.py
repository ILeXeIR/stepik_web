from django import forms
from .models import Question, Answer

class AskForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']
		labels = {'title': 'Title of your question', 'text': "What do you want to ask?"}

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['text', 'question']
		labels = {'text': 'Write your answer', 'question': ''}
