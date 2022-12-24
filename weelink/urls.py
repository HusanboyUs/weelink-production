
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
#stagging packages
from django.shortcuts import render

def userError(request):
    return render(request, 'stagging/index.html')

urlpatterns = [
    path('adminlar/', admin.site.urls),
    path('', include('base.urls')),
    path('accounts/', include('allauth.urls')),
    #api only
    path('api/', include('api.urls')),
    
]
urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
#ssh-keygen -t rsa -b 4096 -C “husanghost@gmail.com”
