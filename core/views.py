from django.shortcuts import render,redirect
from .models import label, data
from .forms import dataForm
from datetime import datetime
from django.http import FileResponse, Http404

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

def video_upload(request):
    media_files = dataForm()
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        title = request.POST['title']
        description = request.POST['description']
        file_type = 'video'

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

    return render(request, 'video_upload.html', {'files': media_files})

def audio_upload(request):
    media_files = dataForm()
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        title = request.POST['title']
        description = request.POST['description']
        file_type = 'audio'

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

    return render(request, 'audio_upload.html', {'files': media_files})


def records(request):
    data = label.objects.all()

    return render(request, 'record.html', {'data':data})

def individual_record(request, id):
    labelx = label.objects.get(id=id)
    datax = data.objects.filter(label=labelx)

    return render(request, 'individual_record.html', {'labels':datax,'label':labelx})

import os

def download_file(request, label_id):
    """
    Retrieves the image file associated with the label and returns it as a downloadable attachment.
    """
    try:
        # Get the label object by its primary key.
        label = data.objects.get(pk=label_id)
    except data.DoesNotExist:
        raise Http404("Label not found.")

    # Assuming the image is stored using a FileField/ImageField on your model:
    file_path = label.file.path  # This is the absolute path to the file on disk

    # Check if the file exists
    if os.path.exists(file_path):
        # Open the file in binary read mode
        file_handle = open(file_path, 'rb')
        # Use FileResponse to serve the file with an 'attachment' header,
        # so that browsers prompt a download.
        return FileResponse(
            file_handle,
            as_attachment=True,
            filename=os.path.basename(file_path)
        )
    else:
        raise Http404("File does not exist.")