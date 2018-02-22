
from django.conf.urls import url ,include
from django.contrib import admin
admin.autodiscover()


print " i m in main url.py ..........."
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'', include('apps.homx.urls')),
# ]


urlpatterns = [
    url(r'^', include('homx.urls')),
    url(r'^admin/', admin.site.urls),
]