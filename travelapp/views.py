from django.http import HttpResponse
from django.shortcuts import render
from .models import types,newtypes

# Create your views here.


# def about(req):
#     return render(req,"about.html")
# def addition(req):
#     x=int(req.GET['num1'])
#     y=int(req.GET['num2'])
#     res=x+y
#     sub=x-y
#     mul=x*y
#     divs=x/y
#     return render(req,"about.html",{'result':res,'subtraction':sub,'multiplication':mul,'division':divs})


def indexpg(req):
    obj=types.objects.all()
    obj1=newtypes.objects.all()
    return render(req,"index.html",{'result':obj,'result1':obj1})