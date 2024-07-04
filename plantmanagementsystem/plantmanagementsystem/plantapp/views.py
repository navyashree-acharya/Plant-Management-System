from django.shortcuts import render,redirect,get_object_or_404
from .models import Plant
from .forms import Plantform
# Create your views here.
def home(request):
    return render(request, 'home.html')
def index(request):
    return render(request, 'index.html')
def viewplant(request):
    plantlist = Plant.objects.all()
    return render(request, 'viewplant.html',{'plantlist':plantlist})

def addplant(request):
    if(request.method == 'POST'):
        form=Plantform(request.POST,request.FILES)
        if(form.is_valid):
            form.save()
            return redirect(viewplant)
    else:
        form=Plantform()
        return render(request,'addplant.html', {'form':form})

def editplant(request,pk):
    p1=get_object_or_404(Plant,pk=pk)
    if(request.method == 'POST'):
        form=Plantform(request.POST,instance=p1)
        if(form.is_valid):
            book1=form.save()
            return redirect(viewplant)
    else:
        form=Plantform(instance=p1)
        return render(request,'addplant.html', {'form':form})

def deleteplant(request,pk):
    p1=get_object_or_404(Plant,pk=pk)
    p1.delete()
    return redirect(viewplant)