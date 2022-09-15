import site
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ProfileLink)
admin.site.register(Contact)
admin.site.register(Projects)


@admin.register(Profile)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('user','location','bio','slug')