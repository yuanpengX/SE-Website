from django import forms

class AutoGeneratePaperForm(forms.Form):
    Chapter = forms.SelectMultiple()
    SelectNum = forms.IntegerField()
    CheckNum = forms.IntegerField()
    Difficulty = forms.FloatField()
    PaperName = forms.CharField()

class AddQuestionForm(forms.Form):
    Chapter = forms.SelectMultiple()