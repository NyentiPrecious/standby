from django.shortcuts import render

def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def Donate(request):
    return render(request, "Donate.html")
def Partners(request):
    return render(request, "Partners.html")
def contact(request):
    return render(request, "contact.html")
def Programs(request):
    return render(request, "Programs.html")
def blog1(request):
    return render(request, "blog1.html")
def event(request):
    return render(request, "Book-event.html")
def boot(request):
    return render(request, "bootcampsignup.html")


# Create your views here.
