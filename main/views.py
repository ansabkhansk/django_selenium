from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import States, Jobtype1, Jobtype2, Jobs

# Create your views here.

# from django.http import HttpResponse

def index(response):
    return render(response, "main/base.html", {})

@login_required
def state(response):
    result = States.objects.all()
    return render(response, "info/state.html", {'States':result})

@login_required
def category(response):
    result = Jobtype1.objects.all()
    result2 = Jobtype2.objects.all()
    return render(response, "info/category.html", {'Categories':result, 'Subcategories':result2})

@login_required
def subcategory(response):
    result = Jobtype2.objects.all()
    result2 = Jobtype1.objects.all()
    return render(response, "info/subcategory.html", {'Subcategories':result, 'Categories':result2})

@login_required
def job(response):
    result = Jobs.objects.all()
    result2 = Jobtype1.objects.all()
    return render(response, "info/jobs.html", {'Jobs':result, 'Subcategories':result2})
