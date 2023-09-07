from django.shortcuts import render

from app.forms import *
from django.http import HttpResponse
def djforms(request):
    SFO = Studentforms()
    d = {'SFO' : SFO}
    if request.method == 'POST':
        SFDO = Studentforms(request.POST)
        if SFDO.is_valid():
            pass
        else:
            return HttpResponse('Invaild Data')
    return render(request,'djforms.html',d)