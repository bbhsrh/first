from django.contrib import admin
from photo.models import *

# Register your models here.
class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 2
    
# @admin.register(Album)
# class AlbumAdmin(admin.ModelAdmin):
#     inlines = (PhotoInline,)
#     list_display = ('id', 'name', 'description')
   
@admin.register(Region1)
class Region1Admin(admin.ModelAdmin):
    inlines = (PhotoInline,)
    list_display = ('id', 'region1')
@admin.register(Region2)
class Region2Admin(admin.ModelAdmin):
    inlines = (PhotoInline,)
    list_display = ('id', 'region2')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')