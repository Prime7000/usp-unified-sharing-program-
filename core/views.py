from django.shortcuts import render,redirect
from .models import label, data
from .forms import dataForm
from datetime import datetime
# Create your views here.

def home(request):

    return render(request, 'home.html')

def image_upload(request):
    media_files = dataForm()
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        title = request.POST['title']
        description = request.POST['description']
        file_type = 'image'

        now = datetime.now()
        full_datetime = str(now.strftime("%Y-%m-%d %H:%M"))
        categorizer = full_datetime

        obj = label.objects.create(title=title, description=description, categorizer=categorizer, file_type=file_type)
        obj.save()

        for file in files:
            media =  data.objects.create(label=obj, file=file)
            media.save()

        return redirect('core:home')


    return render(request, 'image_upload.html', {'files':media_files})

def records(request):
    data = label.objects.all()

    return render(request, 'record.html', {'data':data})

def individual_record(request, id):
    data = label.objects.get(id=id)

    return render(request, 'individual_record.html', {'data':data})