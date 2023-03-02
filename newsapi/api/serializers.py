from rest_framework import serializers
from .models import News



# class NewsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = News
#         fields = ("id","title", "short_description","full_decsriprion","creation_date","deletion_date")

class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=35)
    short_description = serializers.CharField(max_length=100)
    full_decsriprion = serializers.CharField()
    creation_date = serializers.DateField(read_only=True)
    deletion_date = serializers.DateField(required=False)

    def create(self, validated_data):
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.short_description = validated_data.get("short_description", instance.short_description)
        instance.full_decsriprion = validated_data.get("full_decsriprion", instance.full_decsriprion)
        instance.deletion_date = validated_data.get("deletion_date", instance.deletion_date)
        instance.save()
        return instance
