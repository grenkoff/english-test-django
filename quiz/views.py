from django.shortcuts import render

from .models import Question


def question_list(request):
    questions = Question.objects.all()
    return render(
        request,
        'quiz/question/list.html',
        {'questions': questions}
    )


def results(request):
    return render(request, 'quiz/question/results.html')
