from tkinter import CASCADE
from django.db import models

# Create your models here.
class Paradigm(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural= 'Paradigms'


class Language(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name 
    class Meta:
        verbose_name_plural= 'Languages'

class Programmer(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    language =models.ManyToManyField(Language)

    def __str__(self):
        return self.name

