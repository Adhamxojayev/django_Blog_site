from django.contrib import admin
from .models import PostYoz
from .models import Video
from embed_video.admin import AdminVideoMixin

# Register your models here.

admin.site.register(PostYoz)
admin.site.register(Video)

