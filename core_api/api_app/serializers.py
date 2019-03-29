from rest_framework import serializers
from .models import Key_word

class Key_wordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Key_word
        fields = ('id','key_word')

class Key_wordDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Key_word
        fields = ('id', 'key_word', 'videos')
