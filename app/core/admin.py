from django import forms
from django.contrib import admin
from .models import Gallery, Testimonial
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

# Register your models here.

# admin.site.register(Gallery)
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('type', 'image_name', 'title', 'status','created_at')
        }),
    )
    list_display = ("type", "image_name", "title",'status')
    # search_fields = ("type__startswith",)

#admin.site.register(Testimonial)
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name','designation','rating','description','status')