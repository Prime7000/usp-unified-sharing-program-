from django.shortcuts import render,redirect

# Create your views here.

def home(request):

    return render(request, 'home.html')

def image_upload(request):

    return render(request, 'image_upload.html')

def records(request):

    return render(request, 'record.html')