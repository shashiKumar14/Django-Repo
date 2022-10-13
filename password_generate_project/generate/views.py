from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generate/home.html',{'password':'adfgfddfwqAFVFDGREADFCWASFERAGV'})

def password(request):
    letters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        letters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        letters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        letters.extend(list('0123456789'))

    thepassword=''
    length=int(request.GET.get('length'))
    for i in range(length):
        thepassword+=random.choice(letters)
    return render(request,'generate/password.html',{'password':thepassword})

def about(request):
    return render(request,'generate/about.html')