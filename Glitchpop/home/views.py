from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from home.models import Register
# Create your views here.
def index(request):
    context = {
       
    } 
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')
 
def register(request):
    if request.method == "POST":
        nam=request.POST.get('nam')
        mail=request.POST.get('mail')
        ph=request.POST.get('ph')
        prog=request.POST.get('prog')
        goal=request.POST.get('goal')
        register= Register(nam=nam, mail=mail, ph=ph, prog=prog, goal=goal)
        register.save()
        messages.success(request, 'You have successfully registered!')
    return render(request, 'register.html')
                            

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

  
 