from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Question, Answer

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def index(request):
    questions = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    context = {'questions': page.object_list, 'paginator': paginator, 'page': page}
    return render(request, 'index.html', context)

def popular (request):
    questions = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    context = {'questions': page.object_list, 'paginator': paginator, 'page': page}
    return render(request, 'index.html', context)

def question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answer_set.order_by('-added_at')
    context = {'question': question, 'answers': answers}
    return render(request, 'question.html', context)