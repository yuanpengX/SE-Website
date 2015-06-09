from django import forms

class AutoGeneratePaperForm(forms.Form):
    Chapter = forms.CharField()
    SelectNum = forms.IntegerField()
    CheckNum = forms.IntegerField()
    Difficulty = forms.FloatField()
    PaperName = forms.CharField()

class AddQuestionForm(form.Form):
