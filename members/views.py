from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render 
from  .models import Task
    
def complete(request, pk):
    print(pk)
    markasdonetask = get_object_or_404(Task, pk=pk)
    markasdonetask.is_completed = True
    #markasdonetask.save()
    return redirect('landing') 
