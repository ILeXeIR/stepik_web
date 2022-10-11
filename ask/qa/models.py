from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
import re

# Create your models here.

"""
class Tag(models.Model):
	title = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.title
"""

class QuestionManager(models.Manager): 
	def new(self):
		return self.order_by('-added_at')

	def popular(self):
		return self.order_by('-rating')

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	likes = models.ManyToManyField(User, related_name='question_like_user', blank=True)
	tags = TaggableManager()
	objects = QuestionManager()

	def __str__(self):
		return self.title

	def get_url(self):
		return reverse('qa:question', args=[self.id])

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	likes = models.ManyToManyField(User, related_name='answer_like_user', blank=True)

	def __str__(self):
		return f'answer {self.id}'