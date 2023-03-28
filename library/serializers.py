from rest_framework import serializers 
from . import models

class bookSerializer(serializers.Serializer):
    book_name = serializers.CharField(max_length = 100)
    book_author = serializers.CharField(max_length = 100)
    is_issued =serializers.BooleanField(default = False, allow_null = True)
    issued_to = serializers.CharField(max_length = 100, allow_null = True, required = False, default = None)

    def create(self, validated_data):
        return models.books.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.book_name = validated_data.get('book_name', instance.book_name)
        instance.book_author = validated_data.get('book_author', instance.book_author)
        instance.is_issued = validated_data.get('is_issued', instance.is_issued)
        instance.issued_to = validated_data.get('issued_to', instance.issued_to)
        instance.save()
        return instance