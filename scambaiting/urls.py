from django.urls import path
from scambaiting import views

urlpatterns = [
    path('faqs/', views.faqs),
    path('threads/', views.thread_list),
    path('threads/<int:thread_id>', views.thread_detail)
]