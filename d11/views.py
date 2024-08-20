from django.shortcuts import render
from .models import *

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
# Create your views here.
def thank(request):
    return render(request,'a1.html')




def student_registration(request):
    if request.method == 'POST':
        # p1=user.objects.get(pk=1) #update no 1 field

        form = StudentForm(request.POST) #,instance=p1  (write in line when update line use)
        if form.is_valid():
         
            # Form is valid, process the data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(name)
            print(email)
            print(password)
            reg= user(name=name,email=email,password=password)
            reg.save()
            
           
            
            
            # return HttpResponseRedirect('/a1/')
    else:
        form = StudentForm()
    
    return render(request, 'show_regestration.html', {'form': form})