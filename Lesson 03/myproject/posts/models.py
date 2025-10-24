from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField() # Relates to text area form inputs
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True) # Db will automatically add time and date