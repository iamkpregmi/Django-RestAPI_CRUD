from rest_framework import serializers
from .models import *

class mytodoserialiser(serializers.ModelSerializer):
    class Meta:
        model = mytodo
        fields = "__all__"


