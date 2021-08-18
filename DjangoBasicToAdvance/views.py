from django.shortcuts import HttpResponse, render
def home(request):
    name=['Hadi','Sadi','Joti']
    context={
        'name':name,
    }
    return render(request,'home.html',context)