
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.http import HttpResponse

def userError(request):
    return HttpResponse('This app is now under development')

urlpatterns = [
    path('adminlar/', admin.site.urls),
    path('soon/', include('base.urls')),
    path('accounts/', include('allauth.urls')),
    #api only
    path('api/', include('api.urls')),
    path('',userError,name='for now only'),
]
urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
