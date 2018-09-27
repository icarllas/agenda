'''Agenda url configuration... '''
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', include('events.urls')),
    path('', include('blog.urls')),
]
