from rest_framework import serializers
from ..models import Url

class URLSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Url
        fields = '__all__'