from django import forms

class Studentforms(forms.Form):
    sname = forms.CharField(max_length=100)
    sid = forms.IntegerField()
