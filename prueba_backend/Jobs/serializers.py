from rest_framework import serializers
from .models import Job

class JobItemSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Job
        fields = ('__all__')