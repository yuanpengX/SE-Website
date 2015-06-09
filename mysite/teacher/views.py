from django.shortcuts import render_to_response
from form import AutoGeneratePaperForm
from django.http import Http404
from models import Paper, Question, Score, History
# Create your views here.

def AutoGeneratePaper(request):
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


def PaperAnalysis(request, offset):
    #this view generate PapeAnalysis with ID (get from url)
        if len(offset) is not 20:
            raise Http404()
        Paper = Paper.objects.filter()

def PaperView(request):
    # Here I need to get info of teacher
    TeacherId = ''
    ClassIn = ''
    PaperList = Paper.objects.filter(Creator=TeacherId,ClassId=ClassIn)
    #In module, we use ID and name to create a Paper List
    return render_to_response('',{'PaperList':PaperList})