from rest_framework import fields, serializers
from .models import ptarkalis

class ptarkalisSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=ptarkalis
        fields='__all__'
