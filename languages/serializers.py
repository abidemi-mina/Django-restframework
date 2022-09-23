from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *


class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('url','id', 'name',)
class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ('url','id', 'name','language')

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('url','id', 'name','paradigm')