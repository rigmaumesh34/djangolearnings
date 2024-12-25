from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse

def homes(request):
    print("+"*10)
    people=[
        
        {"name":'neema',"age":23},
        {"name":'anu',"age":23},
        {"name":'vivek',"age":23},
        {"name":'rigma',"age":12    }
     
    ]
    return render(request,"index.html",context={'peoples':people})



