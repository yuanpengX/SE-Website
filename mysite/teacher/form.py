from django import forms

class QuestionSearchForm(forms.Form):
    Chapter = forms.SelectMultiple
    SelectNum = forms.IntegerField
    CheckNum = forms.IntegerField
    Difficulty = forms.FloatField
    PaperName = forms.CharField
    DeadLine = forms.DateTimeField
    #def clean_

class QuestionAddForm(forms.Form):
    Stem = forms.CharField
    OptionA = forms.CharField
    OptionAS = forms.Select
    OptionB = forms.CharField
    OptionBS = forms.Select
    OptionC = forms.CharField
    OptionCS = forms.Select
    OptionD = forms.CharField
    OptionDS = forms.Select