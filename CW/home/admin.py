from django.contrib import admin
from . models import userInfo,stuInfo,feed
# Register your models here.
admin.site.site_header = "JIST Admin"




class userInfoAdmin(admin.ModelAdmin):
    list_display = ('username' , 'password')


class stuInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_no', 'guardian_name', 'caste', 'age', 'nationality', 'gender', 'address', 'status')


class feedAdmin(admin.ModelAdmin):
    list_display = ('name', 'feedback', 'date_time')
    list_filter = 'date_time',



admin.site.register(userInfo, userInfoAdmin)
admin.site.register(stuInfo, stuInfoAdmin)
admin.site.register(feed, feedAdmin)