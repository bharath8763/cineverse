from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from django.conf import settings
from django.conf.urls.static import static


def splash(request):
    return render(request, 'splash.html')


urlpatterns = [
    path('', home), 
    path('', splash, name='splash'),
    path('', include('users.urls')),
    path('movies/', include('movies.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
