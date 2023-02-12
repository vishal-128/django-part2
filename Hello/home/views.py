
from django.shortcuts import HttpResponse,render
# render is used when we return templates
# HttpRespone is used when we want to return string
from home.models import Contact
from datetime import datetime
# Create your views here.
def index (request):
    context={"variable1": "i am vishal",
    "variable2":"this is my website"} #dictionary
    return render(request, 'index.html')
    # return HttpResponse("this is home page")

def service (request):
    return render(request, 'services.html')
    #return HttpResponse("this is service page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def sports(request): #contactUs
    if request.method == 'POST':
        
        name1= request.POST.get("name")
        email2= request.POST.get("email")
        phone3=request.POST.get("phone")
        desc4=request.POST.get("desc")
        contact = Contact(name=name1,email=email2,phone=phone3,desc=desc4,date=datetime.today())
        contact.save()
    return render(request, 'sports.html')
    #return HttpResponse("this is sports page")