from django.contrib import admin
from scambaiting.models import Email, Image, ImageAttachment, Person, Thread, FAQ

admin.site.register(Email)
admin.site.register(Image)
admin.site.register(ImageAttachment)
admin.site.register(Person)
admin.site.register(Thread)
admin.site.register(FAQ)
