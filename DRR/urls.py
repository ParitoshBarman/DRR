from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "DRR Admin"
admin.site.site_title = "DRR Admin Portal"
admin.site.index_title = "Welcome to DRR Researcher Portal"


urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('DRRapp.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


