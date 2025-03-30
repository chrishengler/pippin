from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from scambaiting.models import FAQ, Person, Thread
from scambaiting.serializers import FAQSerializer, PersonSerializer, ThreadSerializer, ThreadDetailSerializer


# Create your views here.
@api_view(['GET'])
def inboxes(request):
    """
    List all people with inboxes
    """
    if request.method == 'GET':
        inbox_havers = Person.objects.filter(has_inbox=True)
        serializer = PersonSerializer(inbox_havers, many=True, context={'request': request})
        return Response(serializer.data)

@api_view(['GET'])
def inbox(request, person_id):
    """
    List all threads containing emails from a given person
    """
    if request.method == 'GET':
        threads = Thread.objects.filter(email__sender__pk=person_id, published=True).distinct()
        serializer = ThreadSerializer(threads, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def thread_list(request):
    """
    List all threads
    """
    if request.method == 'GET':
        threads = Thread.objects.filter(published=True)
        serializer = ThreadSerializer(threads, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def thread_detail(request, thread_id):
    """
    List all emails from a thread
    """
    if request.method == 'GET':
        thread = get_object_or_404(Thread,pk=thread_id, published=True)
        serializer = ThreadDetailSerializer(thread, context={'request': request})
        return Response(serializer.data)

@api_view(['GET'])
def faqs(request):
    """
    List all FAQs
    """
    if request.method == 'GET':
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)