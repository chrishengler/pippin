from django.urls import path
from scambaiting import views

urlpatterns = [
    path('faqs/', views.faqs, name='faqs'),
    path('threads/', views.thread_list, name='thread_list'),
    path('threads/<int:thread_id>', views.thread_detail, name='thread_detail'),
    path('inboxes/', views.inboxes, name='inbox_list'),
    path('inbox/<int:person_id>', views.inbox, name='inbox_detail')
]