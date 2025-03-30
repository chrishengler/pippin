from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from datetime import datetime, timedelta
from faker import Faker
from rest_framework import status

from scambaiting.models import Person, Email, Thread
import scambaiting.views as views

# Create your tests here.
class ViewTests(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.c = Client()
        self.baiter = Person.objects.create(name=self.faker.name(), email_address=self.faker.email(), has_inbox=True, bio=self.faker.sentence())
        self.scammer = Person.objects.create(name=self.faker.name(), email_address=self.faker.email(), has_inbox=False)

    def create_email(self, sender: Person, recipient: Person, thread: Thread, timestamp: datetime = datetime.now()) -> Email:
        new_email = Email.objects.create(sender=sender, recipient=recipient, thread=thread, subject=self.faker.sentence(), body=self.faker.sentences(), timestamp=timestamp)
        return new_email

    def test_inbox_list(self):
        response = self.c.get(reverse('inbox_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], self.baiter.name)
        self.assertEqual(data[0]['email_address'], self.baiter.email_address)
        
    def test_inbox_detail(self):
        response = self.c.get(reverse('inbox_detail', args=[self.baiter.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(len(data), 0)

        thread = Thread.objects.create(title=self.faker.sentence())
        self.create_email(self.baiter, self.scammer, thread)
        self.create_email(self.scammer, self.baiter, thread)
        
        response = self.c.get(reverse('inbox_detail', args=[self.baiter.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(len(data), 1)

    def test_thread_detail(self):
        thread = Thread.objects.create(title=self.faker.sentence())
        self.create_email(self.baiter, self.scammer, thread, timestamp=datetime.now()-timedelta(hours=1))
        self.create_email(self.scammer, self.baiter, thread)
        
        response = self.c.get(reverse('thread_detail', args=[thread.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        print(data)
        self.assertEqual(len(data), 2)
        self.assertEqual(data['title'], thread.title)
        emails = data['emails']
        self.assertEqual(emails[0]['sender']['pk'], self.baiter.pk)
        self.assertEqual(emails[1]['sender']['pk'], self.scammer.pk)
