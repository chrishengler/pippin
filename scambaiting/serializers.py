from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()
    name = serializers.CharField(required=False)

class PersonSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    name = serializers.CharField()
    display_image = ImageSerializer(required=False)

class ThreadSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    title = serializers.CharField()

class ImageAttachmentSerializer(serializers.Serializer):
    image = ImageSerializer()

class EmailSerializer(serializers.Serializer):
    timestamp = serializers.DateTimeField()
    recipient = PersonSerializer()
    sender = PersonSerializer()
    cc = PersonSerializer(many=True)
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
