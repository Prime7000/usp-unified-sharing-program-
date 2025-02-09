from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.home, name = 'home'),
    path('image_upload', views.image_upload, name = 'image_upload'),
    path('video_upload', views.video_upload, name = 'video_upload'),
    path('audio_upload', views.audio_upload, name = 'audio_upload'),
    path('records/', views.records, name = 'record'),
    path('records/<int:id>', views.individual_record, name = 'individual_record'),
    path('download/<int:label_id>/', views.download_file, name='download_file')
]