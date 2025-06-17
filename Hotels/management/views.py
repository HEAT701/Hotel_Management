from django.shortcuts import render
from  .models import Hotel
# Create your views here.



def List_Hotel(request):
    data = Hotel.objects.all().values()
    return render(request,'index.html',{"data":data})