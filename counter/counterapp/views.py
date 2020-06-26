from django.shortcuts import render,redirect
from .models import CounterModel
# Create your views here.
def helloworld(request):
    name = "Nikita"
    obj = CounterModel.objects.filter(id=1)[0]
    ournumber = obj.number
    dic =  {"name" : name, "number":ournumber} #for passing a variable
    return render(request,"helloworld/helloworld.html",dic) # helloworld.html from templates
    # passing python variables in html template

def increment(request): #code to increment number
    obj = CounterModel.objects.filter(id = 1)[0]
    obj.number = int(obj.number) + 1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

def decrement(request):
    obj = CounterModel.objects.filter(id=1)[0]
    obj.number = int(obj.number) - 1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

def reset(request):
    obj = CounterModel.objects.filter(id = 1)[0]
    obj.number = 0
    obj.save()
    return redirect(request.META['HTTP_REFERER'])
