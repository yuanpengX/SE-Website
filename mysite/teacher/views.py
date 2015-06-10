from django.shortcuts import render_to_response
from form import AutoGeneratePaperForm
from django.http import Http404
from models import Paper, Question, Score, History
import re
import os
from django.template.context import RequestContext
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group,Permission
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Create your views here.

def PaperAutoGenerate(request):
    # here we need user_auth
    if request.POST:
        form = AutoGeneratePaperForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Ch = cd.Chapter
            SNum = cd.SelectNum
            CNum = cd.CheckNum
            Diff = cd.Difficulty
            ##select question from DB
            ChQuesList = Question.objects.filter(Chapter__contains=Ch, Type=0).order_by('Difficulty')
            SelQuesList = Question.objects.filter(Chapter__contains=Ch, Type=1).order_by('Difficulty')
            QuestList = [ChQuesList, SelQuesList]
            return render_to_response('PaperView.html', {'QuestList': QuestList})
    else:
        form = AutoGeneratePaperForm(request.POST)
    return render_to_response('', {'form': form})

def PaperManualGenerate(request):
    return render_to_response('',locals())

def PaperAnalysis(request, offset):
    #this view generate PapeAnalysis with ID (get from url)
    PaperView = False
    AuthError = False
    if request.user.is_authenticated():
        if len(offset) is not 20:  # LENGTH is exactly 20
            raise Http404()
        else:
            try:
                tmp = long(offset) # MUST be pure number
            except ValueError:
                raise Http404()
        ''' Gengerate Analysis Result
            Here we use lib to generate pic
        '''
        # get score
        PaperL = Paper.objects.filter(PaperId=offset)
        QuesId = PaperL['QId']
        QuestionList = []
        for i in range(len(QuesId)):
            QuestionList[i]
    else:
        AuthError = True
    return render_to_response('',{'AuthError':AuthError,'QuestionList':QuestionList,'PaperView':PaperView})

def PaperView(request,offset):
    #this view generate PapeAnalysis with ID (get from url)
    AuthError = False
    Paperview = True
    if request.user.is_authenticated():
        if len(offset) is not 20:  # LENGTH is exactly 20
            raise Http404()
        else:
            try:
                tmp = long(offset) # MUST be pure number
            except ValueError:
                raise Http404()
        ''' Gengerate Analysis Result
            Here we use lib to generate pic
        '''
        PaperL = Paper.objects.filter(PaperId=offset)
        QuesId = PaperL['QId']
        QuestionList = []
        for i in range(len(QuesId)):
            QuestionList[i] = Question.objects.filter(QuestionId=QuesId[i*20:i+19])
    else:
        AuthError = True
    return render_to_response('',{'AuthError':AuthError,'QuestionList':QuestionList,'PaperView':PaperView})

def QuestionModify(request):
    return render_to_response('',locals());

def QuestionDelete(request):
    return render_to_response('',locals())

def QuestionAdd(request):
    return render_to_response('',locals())