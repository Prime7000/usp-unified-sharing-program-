from django.db import models

# Create your models here.

class label(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    categorizer = models.CharField(max_length=100, null=True, blank=True)
    file_type = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(upload_to='thumbnail/', null=True, blank=True)

    def __str__(self):
        return self.categorizer
    

class data(models.Model):
    label = models.ForeignKey(label, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.label.categorizer