from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^doafrica/', include('doafrica.urls')),
   # url(r'^opt/', include('opt.urls')),
   ] + static ( settings.MEDIA_URL , document_root =settings.MEDIA_ROOT )