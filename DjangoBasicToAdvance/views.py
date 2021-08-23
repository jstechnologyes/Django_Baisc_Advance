from django.shortcuts import HttpResponse, render
from tuition.models import Contact
def home(request):
    if request.method=="GET":
        name=['Hadi','Sadi','Joti']
    else:
        name=[]
    context={
        'name':name,
    }
    return render(request,'home.html',context)

