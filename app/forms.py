from django import forms

class Studentforms(forms.Form):
    sname = forms.CharField(max_length=100)
    sid = forms.IntegerField()
    smark = forms.FloatField()
    spercentage = forms.FloatField()
    sdob = forms.DateField()
    semail = forms.EmailField()
    Sclasstime = forms.TimeField()
    Surl=forms.URLField()
    sdrop = forms.ChoiceField()
    sdroplist= forms.CharField(widget= forms.PasswordInput)
    stext = forms.CharField(widget=forms.Textarea)
    schoicefiles= forms.ChoiceField(widget=forms.RadioSelect)
    smulch= forms.MultipleChoiceField(widget=forms.CheckboxInput)
    # sslug= forms.SlugField() # invalid