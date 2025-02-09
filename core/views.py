from django.shortcuts import render,redirect
from .models import label, data
from .forms import dataForm
from datetime import datetime
# Create your views here.

def home(request):

    return render(request, 'home.html')

from datetime import datetime
from django.shortcuts import redirect, render

def image_upload(request):
    media_files = dataForm()
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        title = request.POST['title']
        description = request.POST['description']
        file_type = 'image'

        # Get the first file from the uploaded files list as the thumbnail
        thumbnail = files[0] if files else None

        now = datetime.now()
        full_datetime = now.strftime("%Y-%m-%d %H:%M")
        categorizer = full_datetime

        # Create the label object including the thumbnail
        obj = label.objects.create(
            title=title,
            description=description,
            categorizer=categorizer,
            file_type=file_type,
            image=thumbnail  # Make sure your model has this field
        )
        obj.save()

        # Save all uploaded files associated with this label
        for file in files:
            media = data.objects.create(label=obj, file=file)
            media.save()

        return redirect('core:home')

    return render(request, 'image_upload.html', {'files': media_files})


def records(request):
    data = label.objects.all()

    return render(request, 'record.html', {'data':data})

def individual_record(request, id):
    labelx = label.objects.get(id=id)
    datax = data.objects.filter(label=labelx)

    return render(request, 'individual_record.html', {'labels':datax,'label':labelx})