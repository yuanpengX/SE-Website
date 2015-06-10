from django.shortcuts import render_to_response
from form import QuestionSearchForm,QuestionAddForm
from django.http import Http404,HttpResponseRedirect
from math import exp
import random
from models import Paper, Question, Score, History
import datetime
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

#finish0.9
def SelectQuestion(Ch,Type_i,Num,Diff):
    SelectQue = []
    mysum = 0
    for i in [2,3,4,5]:
        p = exp(-abs(i-Diff))
        NumQ = round(Num*p)
        mysum +=NumQ
        Q = Question.objects.filter(Chapter_in=Ch, Type=Type_i, Difficulty=i)
        if len(Q)<NumQ:
            return []
        else:
            random.sample(Q, NumQ)
            SelectQue.append(Q)
    Q = Question.objects.filter(Chapter_in=Ch, Type=Type_i, Difficulty=i)
    NumQ = Num-mysum
    if len(Q)<NumQ:
        return []
    else:
        random.sample(Q,NumQ)
        SelectQue.append(Q)
    return SelectQue
#finish0.9
def PaperAutoGenerate(request):
    # here we need user_auth
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/user_auth/');
    if request.POST:
        form = QuestionSearchForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Ch = cd['Chapter']
            SNum = cd['SelectNum']
            JNum = cd['CheckNum']
            Diff = cd['Difficulty']
            Name = cd['PaperName']
            Dead =cd['DeadLine']
            ##select question from DB
            # select algorithm
            ChL = SelectQuestion(Ch, 0, SNum, Diff)
            if not ChL:
                form.errors.append('Not Enough Multiple Choice Question')
            #JudQuesList = Question.objects.filter(Chapter__in=Ch, Type=1).order_by('Difficulty')
            JuL = SelectQuestion(Ch, 1, JNum, Diff)
            if not JuL:
                form.errors.append('Not Enough Judge Question')
            QuestList = [ChL, JuL]
            # add paper into database
            Qid = ''
            for question in QuestList:
                Qid = Qid + question.QuestionId
            paperid = re.sub(r'-:\\.\\ ',str(datetime.datetime.now))
            paperid = request.user.name + paperid[0:15]
            Paper.objects.create(PaperId= paperid,
                                PaperName = Name,
                                QId = Qid,
                                Creator = request.user.name,
                                # jfaj
                                ClassId = ClassId,
                                StartTime = datetime.datetime.now(),
                                Deadline = Dead )
            return render_to_response('PaperView.html', {'QuestList': QuestList})
    else:
        form = QuestionSearchForm()
    return render_to_response('', {'form': form})

def PaperManualGenerate(request):

    return render_to_response('',locals())

def PaperAnalysis(request, offset):
    #this view generate PapeAnalysis with ID (get from url)
    PaperView = False
    AuthError = False
    if request.user.is_authenticated():
        try:
           PaperL = Paper.objects.filter(PaperId=offset)
        except Paper.DoesNotExist:
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
#finish0.9
def PaperView(request,offset):
    #this view generate PapeAnalysis with ID (get from url)
    Paperview = True
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/user_auth/')
    else:
        try:
           PaperL = Paper.objects.filter(PaperId=offset)
        except Paper.DoesNotExist:
           raise Http404()
        ''' Gengerate Analysis Result
            Here we use lib to generate pic
        '''
        QuesId = PaperL['QId']
        QuestionList = []
        for i in range(len(QuesId)):
            QuestionList[i] = Question.objects.filter(QuestionId=QuesId[i*20:i*20+19])
    return render_to_response('paper.html',{'QuestionList':QuestionList,'view':PaperView})

def QuestionModify(request):
    return render_to_response('',locals());

def QuestionDelete(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/user_auth/')
    if request.POST:
        form1 = QuestionSearchForm(request.POST)
        if form1.is_valid():
            form1
    return render_to_response('',locals())

def QuestionAdd(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/user_auth/')
    if request.POST:
        form = QuestionAddForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            QuestionStem = cd.
        else:
            return render_to_response('',{'form':form})
    return render_to_response('',locals())
