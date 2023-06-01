from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'homepage.html')
def jobs(request):
    return render(request,'jobs.html')
def jobfair(request):
    return render(request,'jobfair.html')
def aboutpage(request):
    return render(request,'about.html')
