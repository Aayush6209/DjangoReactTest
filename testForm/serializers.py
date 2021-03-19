from django.db.models import fields
from rest_framework import serializers
from .models import User

# these are serializers


class UserSerializer(serializers.ModelSerializer):
    # copy fields from models.py
    class Meta:
        model = User
        fields = '__all__'
