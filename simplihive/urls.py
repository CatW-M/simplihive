from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#Configure Admin Titles
admin.site.site_header = "Simplihive Admin Page"
admin.site.site_title = "Browser Title"
admin.site.index_title = "Welcome to the Admin Area"