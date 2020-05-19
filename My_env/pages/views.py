from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,"home.html",{})

def contact_view(request, *args, **kwargs):
    return render(request,"contact.html",{})

def about_view(request, *args, **kwargs):
    my_context = {
       "title":"nayemul hasan saheb",
        "my_number": 1760988571,
        "my_list" :[2015,"macuc","Dhaka"],
        "my_html": "<h1>Test web Project</h1>"
    }
    return render(request,"about.html", my_context)