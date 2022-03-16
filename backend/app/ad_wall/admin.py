from django.contrib import admin

from .models import Ad, Image


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
