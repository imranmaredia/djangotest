from django.shortcuts import render 
from members.models import Task
def home(request):
            #return HttpResponse('<h1> homepage</h1>')
                 #tasks = workdetails.objects.all #This will filter ALL DATA
                rawdata = Task.objects.all()
                context = {
                        'dictTask':rawdata,
                     #   'dictcomplete':completedtask,
                     }

                return render(request, 'Main.html',context) 
