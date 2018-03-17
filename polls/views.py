# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Question, Choise

class IndexView(generic.ListView):
    template_name ='polls/index.html'
    context_object_name='latest_questions_list'

    def get_querySet(self):
        "Return the las five publushed question"
        return Question.object.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model=Question
    template_name ='polls/detail.html'


class ResultView(generic.DetailView):
    model=Question
    template_name ='polls/result.html'

def vote(request, question, id):
    question=get_object_or_404(Question, pk = question_id)
    try:
        selected_choise = question.choise_set.get(pk=request.POST['choise'])
    except(KeyError, choise.DoesNotExist):
        return render (request, 'polls/details.htmal',{
            'question':question,
            'error_message':"no seleccionaste ninguna opcion"
        })

    else:
        selected_choise.votes +=1
        selected_choise.save()
        return HttpResponseRedirect(reverse(
        'polls:results', arg=(question.id,)))
    