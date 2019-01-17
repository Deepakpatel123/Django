from django.shortcuts import render
from django.http import HttpResponse
from emailexample import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'index.html')
    

def mail(request):
    
    to=request.GET['To']
    print('kk')
    subject=request.GET['Subject']
    print('kk11')
    msg=request.GET['myTextarea']
    res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
    if(res==1):
        msg="Mail sent successfuly"
    else:
        msg="Mail COuld Not sent"
    return HttpResponse(msg)
