from django.shortcuts import render,redirect
from . form import todoforms
from . models import Todo
from django .http import HttpResponse

# Create your views here.
def home(request):
    form=todoforms()
    todos=Todo.objects.all()
    context = {
        'form':form,
        'todos':todos
    }  
    if request.method=='POST':
        form=todoforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request,'index.html',context)

def delete(request,id):
    todo=Todo.objects.get(id=id)
    if request.method=='POST':
        todo.delete()
        return redirect('home')


