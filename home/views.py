from django.shortcuts import render, redirect
from .models import Visitor
from .forms import VisitorForm

# Create your views here.
def welcome_home(request):
    if request.method == "POST":
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("home:welcome_home")
    
    visitors = Visitor.objects.all()
    form = VisitorForm()
    context = {
        'visitors' : visitors,
        'form' : form,
    }

    return render(request, 'home/welcome_home.html', context)
