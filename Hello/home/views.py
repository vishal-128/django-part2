
from django.shortcuts import HttpResponse,render
# render is used when we return templates
# HttpRespone is used when we want to return string

# Create your views here.
def index (request):
    context={"variable1": "i am vishal",
    "variable2":"this is my website"} #dictionary
    return render(request, 'index.html')
    # return HttpResponse("this is home page")

def service (request):
    return HttpResponse("this is service page")

def about(request):
    return HttpResponse("this is about page")

def sports(request):
    return HttpResponse("this is sports page")