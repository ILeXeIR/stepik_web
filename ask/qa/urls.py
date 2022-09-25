#URLs for app 'qa'

from django.urls import path
from . import views

app_name = 'qa'
urlpatterns = [
	path('', views.test, name='index'),
	path('login/', views.test, name='login'),
	path('signup', views.test, name='signup'),
	path('question/<int:question_id>/', views.test, name='question'),
	path('ask/', views.test, name='ask'),
	path('popular/', views.test, name='popular'),
	path('new/', views.test, name='new'),
]

"""
/
/login/
/signup/
/question/<123>/    # вместо <123> - произвольный ID
/ask/
/popular/
/new/
"""