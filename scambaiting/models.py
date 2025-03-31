from django.conf import settings
from django.db import models
from django.db.models import Model

from scambaiting.validators import no_spaces


class Image(Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        if self.name:
            return self.name
        return self.id


class Person(Model):
    name = models.CharField(max_length=200)
    display_image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.PROTECT)
    has_inbox = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)
    email_address = models.CharField(max_length=100, blank=True, null=True)
    baiter = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class Thread(Model):
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=False)
    correspondents = models.ManyToManyField(Person, blank=True)
    
    def __str__(self):
        return self.title


class Email(Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    recipient = models.ForeignKey(Person, on_delete=models.PROTECT, related_name="recipient")
    sender = models.ForeignKey(Person, on_delete=models.PROTECT, related_name="sender")
    subject = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    cc = models.ManyToManyField(Person, blank=True)

    def __str__(self):
        return f"'{self.subject}' sent by {self.sender} to {self.recipient} at {self.timestamp}"

    class Meta:
        ordering = ['timestamp']


class ImageAttachment(Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.PROTECT)


class FAQ(Model):
    question = models.TextField()
    answer = models.TextField()
    short_id = models.CharField(max_length=50, unique=True, validators=[no_spaces])

    def __str__(self):
        return f"FAQ:{self.short_id}: {self.question}"
