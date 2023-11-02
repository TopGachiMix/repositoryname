from typing import Any
from django.contrib import admin
from django.utils.html import format_html

from .models import advertisement
from django.db import models
from django.conf import settings
# 'created_at','created_date'
class advertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'updated_date', 'auction', 'image','image_preview']
    list_filter = ['auction', 'created_at']
    auction = ['make_auction_as_false']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        obj.save()


    def image_preview(self,obj):
         if obj.image:
            return format_html('<img src="{}" width="100" height="100" />',obj.image.url)
         else:
          default_image_url = settings.STATIC_URL + 'img/adv.png'
          return format_html('<img src="{}" width="100" height="100" />',default_image_url)




admin.site.register(advertisement, advertisementAdmin)