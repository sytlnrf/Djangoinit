from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice


def index(request):
    all_q = Question.objects.first()
    return HttpResponse(all_q)
