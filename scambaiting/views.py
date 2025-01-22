from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from scambaiting.models import FAQ, Thread
from scambaiting.serializers import FAQSerializer, ThreadSerializer, ThreadDetailSerializer


# Create your views here.
@api_view(['GET'])
def thread_list(request):
    """
    List all threads
    """
    if request.method == 'GET':
        threads = Thread.objects.all()
        serializer = ThreadSerializer(threads, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def thread_detail(request, thread_id):
    """
    List all emails from a thread
    """
    if request.method == 'GET':
        thread = get_object_or_404(Thread,pk=thread_id)
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