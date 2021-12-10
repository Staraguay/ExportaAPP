from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):

    return render(request, "index.html")

def details(request,pk):

    if pk == 1:

        return render(request,"details.html")
    elif pk == 2:
        return render(request,"details2.html")
    elif pk == 3:
        return render(request,"details3.html")
    else:
        return HttpResponse("")