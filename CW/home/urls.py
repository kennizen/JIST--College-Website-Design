from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_page),
    path('login', views.login_page),
    path('registration', views.registration_page),
    path('stuinfo/<name>', views.stu_info),
    path('feedback', views.feedback),
    path('notice', views.notice),
    path('it', views.it),
    path('library', views.library),
    path('hostel', views.hostel),
    path('bog', views.bog),
    path('humanities', views.humanities),
    path('maths', views.maths),
    path('etc', views.etc),
    ]
