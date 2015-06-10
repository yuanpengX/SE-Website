from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.

def ViewPaper(request):
    AuthError = False
    if request.user.is_authenticated():
        StudentId = request.user.name
    else:
        AuthError = True
    return render_to_response('OnlineTest',locals())

def OnlinePaper(request):
    AuthError = False
    if request.user.is_authenticated():
        # generate question list
        StudentId = request.user.name
    else:
        AuthError = True

def ReturnScore(request):
    return render_to_response('',locals())