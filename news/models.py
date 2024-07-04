from django.db import models

# Create your models here.
class NewsItem(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title