from django.shortcuts import render
from django.shortcuts import render_to_response
from django.Http import   HttpResponseRedirect
from teacher.models import Paper,Score
# Create your views here.
def ViewPaper(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/user_auth/')
    if request.method =='GET':
        PaperIdList = Paper.objects.filter(ClassId = ClassID)
        for paperid in PaperIdList:
            P = Score.objects.filter(StudentId=request.user.name,ClassId=ClassID)
            paperid['MaxScore'] = P.MaxScore
            paperid['ValidScore'] = P.ValidScore
            paperid['SubmitTime'] = P.SubmitTime
            paperid['URL'] = request.get_host+'/paper/'+paperid.PaperId
        return render_to_response('OnlineTest',{'PaperList':PaperIDList})

def OnlinePaper(request):
    AuthError = False
    if request.user.is_authenticated():
        # generate question list
        StudentId = request.user.name
    else:
        AuthError = True

def ReturnScore(request):

    return render_to_response('',locals())