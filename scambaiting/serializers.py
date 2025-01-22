from rest_framework import serializers

from scambaiting.models import Thread

class ThreadSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    title = serializers.CharField()

    def create(self, validated_data):
        return Thread.objects.create(**validated_data)

class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()
    name = serializers.CharField(required=False)

class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    display_image = ImageSerializer(required=False)

class ImageAttachmentSerializer(serializers.Serializer):
    image = ImageSerializer()

class EmailSerializer(serializers.Serializer):
    timestamp = serializers.DateTimeField()
    recipient = PersonSerializer()
    sender = PersonSerializer()
    subject = serializers.CharField()
    body = serializers.CharField()
    initial_comment = serializers.CharField(required=False)
    final_comment = serializers.CharField(required=False)
    image_attachments = ImageAttachmentSerializer(many=True, required=False, source='imageattachment_set')
    entry = serializers.IntegerField()

class ThreadDetailSerializer(serializers.Serializer):
    title = serializers.CharField()
    emails = EmailSerializer(many=True, source="email_set")

class FAQSerializer(serializers.Serializer):
    short_id = serializers.CharField()
    question = serializers.CharField()
    answer = serializers.CharField()
