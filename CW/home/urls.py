from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_page),
    path('login', views.login_page),
    path('registration', views.registration_page),
    path('stuinfo/<name>', views.stu_info),
    path('feedback', views.feedback),
    path('notice-1/<name>', views.notice_1),
    path('notice-2', views.notice_2),
    path('dept-IT-1/<name>', views.dept_IT_1),
    path('dept-IT-2', views.dept_IT_2),
    ]
