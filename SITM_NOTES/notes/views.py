from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from notes.models import Contact,Notes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        desc = request.POST.get('desc')

        contact = Contact(name = name, email= email,subject= subject,desc=desc,date= datetime.today())
        contact.save()
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username= username, password= password)
        if user is not None :
            login(request,user)
            return redirect("/")
        else :
            return render(request, 'login.html')
    return render(request, 'login.html')
def registerUser(request):
    if request.method == 'POST':
        n = request.POST.get("name")
        s = n.split(" ")
        firstname = s[0]
        lastname = s[1]
        username = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username,username, password)
        user.last_name = lastname
        user.first_name = firstname
        if user is not None :
            user.save()
            return redirect("/")
        else :
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/")

def about(request):
    return render(request, 'about.html')

def downloadnotes(request):
    return render(request, 'downloadnotes.html')

def impupdate(request):
    return render(request, 'impupdate.html')

def downloadsection(request):
    branch = request.POST.get('r')
    sem = request.POST.get('radio2')
    data = Notes.objects.all()
    n =[]
    for i in data:
        if i.sem+i.branch == sem+branch :
            n.append(i)
    if len(n) == 0:
        return render(request,'downloadsection.html')
    p = {
        "notes":n,
        "sem":n[0].sem,
        "branch":n[0].branch
    }
    print(n)
    return render(request, 'downloadsection.html',p)

