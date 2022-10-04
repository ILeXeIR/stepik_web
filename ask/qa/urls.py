#URLs for app 'qa'

from django.urls import path
from . import views

app_name = 'qa'
urlpatterns = [
	path('', views.index, name='index'),
	path('login/', views.user_login, name='login'),
	path('logout/', views.user_logout, name='logout'),
	path('signup/', views.signup, name='signup'),
	path('question/<int:question_id>/', views.question, name='question'),
	path('ask/', views.ask, name='ask'),
	path('popular/', views.popular, name='popular'),
	path('new/', views.test, name='new'),
]

