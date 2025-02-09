from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.home, name = 'home'),
    path('image_upload', views.image_upload, name = 'image_upload'),
    path('records/', views.records, name = 'record'),
    path('records/<int:id>', views.individual_record, name = 'individual_record'),
]