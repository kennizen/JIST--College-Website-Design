from django.contrib import admin
from . models import userInfo,stuInfo,feed
# Register your models here.
admin.site.site_header = "JIST admin"

admin.site.register(userInfo)
admin.site.register(stuInfo)
admin.site.register(feed)
