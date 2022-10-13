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

def tagged (request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    questions = Question.objects.filter(tags=tag)
    limit = request.GET.get('limit', 5)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = f'/tagged/{slug}/?page='
    page = paginator.page(page)
    context = {'questions': page.object_list, 'paginator': paginator, 'page': page, 'tag': tag}
    return render(request, 'index.html', context)


def question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answer_set.order_by('-added_at')
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
    context = {'question': question, 'answers': answers, 'form': form}
    return render(request, 'question.html', context)

def ask(request):
    if request.method != 'POST':
        form = AskForm()
    else:
        form = AskForm(data=request.POST)
        if form.is_valid():
            ask = form.save(commit=False)
            ask.author = request.user
            ask.save()
            form.save_m2m()
            url = ask.get_url()
            return redirect(url)
    context = {'form': form}
    return render(request, 'ask.html', context)

