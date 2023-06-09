from django.db import models

# Create your models here.
class About(models.Model):
    desc1=models.CharField( max_length=255)
    desc2=models.CharField( max_length=255)
    bday=models.CharField( max_length=255)
    web=models.CharField( max_length=255)
    phone=models.CharField( max_length=255)
    city=models.CharField( max_length=255)
    age=models.IntegerField()
    deg=models.CharField( max_length=255)
    mail=models.CharField( max_length=255)
    dispo=models.CharField( max_length=255)
    desc3=models.CharField( max_length=255)
    
class Skills(models.Model):
    name=models.CharField( max_length=255)
    level = models.PositiveIntegerField()

class Services(models.Model):
    titre = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    ICON_CHOICES = [
        ('bi-briefcase', 'briefcase'),
        ('bi-card-checklist', 'checklist'),
        ('bi-bar-chart', 'chart'),
        ('bi-binoculars', 'binoculars'),
        ('bi-brightness-high', 'brightness-high'),
        ('bi-calendar4-week', 'calendar4-week'),
    ]
    icon = models.CharField(max_length=250, choices=ICON_CHOICES)
    
class Testi(models.Model):
    name=models.CharField( max_length=255)
    job=models.CharField( max_length=255)
    desc=models.CharField( max_length=255)
    IMG_CHOICES =[
        ('testimonials-1.jpg','image 1'),
        ('testimonials-2.jpg','image 2'),
        ('testimonials-3.jpg','image 3'),
        ('testimonials-4.jpg','image 4'),
        ('testimonials-5.jpg','image 5'),
    ]
    img=models.CharField( max_length=255, choices=IMG_CHOICES )

class Contact(models.Model):
    loc=models.CharField( max_length=255)

class Cont(models.Model):
    loc=models.CharField( max_length=255)
    mail=models.CharField( max_length=255)
    phone=models.CharField( max_length=255)
    
class Filtre(models.Model):
    filtre=models.CharField( max_length=255)
    
class Porto(models.Model):
    IMG_CHOICES =[
        ('portfolio-1.jpg','image 1'),
        ('portfolio-2.jpg','image 2'),
        ('portfolio-3.jpg','image 3'),
        ('portfolio-4.jpg','image 4'),
        ('portfolio-5.jpg','image 5'),
        ('portfolio-6.jpg','image 6'),
        ('portfolio-7.jpg','image 7'),
        ('portfolio-8.jpg','image 8'),
        ('portfolio-9.jpg','image 9'),
    ]
    img=models.CharField( max_length=255, choices=IMG_CHOICES)
    filtre=models.CharField( max_length=255)

