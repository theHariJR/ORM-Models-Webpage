from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=20,primary_key=True)

    def __str__(cls):
        return cls.topic_name
    
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    url=models.URLField()
    email=models.EmailField()
    

    def __str__(cls):
        return cls.name
    

class Accessrecord(models.Model):
    name=models.ForeignKey(Webpage, on_delete=models.CASCADE)
    author=models.CharField(max_length=25)
    date=models.DateField()

    def __str__(cls):
        return cls.author
    
    