from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from taggit.models import Tag
from .models import *
from .forms import *

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def index(request):
    questions = Question.objects.new()
    limit = request.GET.get('limit', 5)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    context = {'questions': page.object_list, 'paginator': paginator, 'page': page}
    return render(request, 'index.html', context)

def popular (request):
    questions = Question.objects.popular()
    limit = request.GET.get('limit', 5)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    context = {'questions': page.object_list, 'paginator': paginator, 'page': page}
    return render(request, 'index.html', context)

def question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answer_set.order_by('-added_at')
    tags = list(question.tags.names())
    if request.method != 'POST':
        form = AnswerForm()
    else:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            url = question.get_url()
            return redirect(url)
    context = {'question': question, 'answers': answers, 'tags': tags, 'form': form}
    return render(request, 'question.html', context)

def ask(request):
    if request.method != 'POST':
        form = AskForm()
    else:
        form = AskForm(data=request.POST)
        if form.is_valid():
            ask = form.save(commit=False)
            #ask = Question(**form.cleaned_data)
            #ask.title = form.title
            #ask.text = form.text
            #ask.tags = form.tags
            ask.author = request.user
            ask.save()
            form.save_m2m()
            url = ask.get_url()
            return redirect(url)
    context = {'form': form}
    return render(request, 'ask.html', context)

"""
def user_login(request):
    error=''
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('qa:index')
        else:
            error = "Login failed. Try again."
    context = {'form': form, 'error': error}
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    context = {'form': LoginForm(), 'error': 'You have logged out'}
    return render(request, 'login.html', context)

def signup(request):
    if request.method != 'POST':
        form = RegisterForm()
    else:
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST.get('password'))
            user.save()
            login(request, user)
            return redirect('qa:index')
    context = {'form': form}
    return render(request, 'signup.html', context)
"""
