# i made this - swarnava

from django.shortcuts import render
from django.http import HttpResponse

def index(r):
    return render(r,'index.html')

def result(r):
    djtext=r.POST.get('text','default')

    up=r.POST.get('up','off')
    cc=r.POST.get('cc','off')
    nlr=r.POST.get('nlr','off')

    count=0
    if(up=='on'):
        djtext =  djtext.upper()
    if(nlr=='on'):
       djtext=djtext.replace('\n','').replace('\r','')
    if(cc=='on'):
        count=len(djtext)
    if(up!='on' and cc!='on' and nlr!='on'):
        return HttpResponse('Error')
    
    paeams={'cc':'Your result','at':djtext,'ac':count}
    return render(r,'result.html',paeams)
