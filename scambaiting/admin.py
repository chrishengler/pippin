from django.contrib import admin
from scambaiting.models import Email, Image, ImageAttachment, Person, Thread, FAQ

class ImageAttachmentInlineAdmin(admin.StackedInline):
    model = ImageAttachment

class EmailAdmin(admin.ModelAdmin):
    inlines = [ImageAttachmentInlineAdmin]
    
admin.site.register(Email, EmailAdmin)
admin.site.register(Image)
admin.site.register(ImageAttachment)
admin.site.register(Person)
admin.site.register(Thread)
admin.site.register(FAQ)
