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

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        content=request.POST['content']
        obj=Contact(name=name,phone=phone,content=content)
        obj.save()
    return render(request,'contact.html')