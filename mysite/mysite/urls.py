from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('joy/', include('joystick.urls')),
    path('admin/', admin.site.urls),
    path('', include('connect.urls')),
]