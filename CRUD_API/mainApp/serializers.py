from rest_framework import serializers
from .models import *

class productsSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = "__all__"


