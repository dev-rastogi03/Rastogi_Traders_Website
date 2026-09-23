from django.contrib import admin
from django.utils.html import format_html
from .models import CropGuide, FarmerTip


@admin.register(CropGuide)
class CropGuideAdmin(admin.ModelAdmin):
    list_display = (
        'icon_badge', 'crop_name_hi', 'crop_name_en', 'season', 
        'sowing_time', 'is_featured', 'is_active', 'display_order'
    )
    list_editable = ('is_featured', 'is_active', 'display_order')
    search_fields = ('crop_name_hi', 'crop_name_en', 'summary', 'fertilizer_schedule')
    fields = (
        'crop_name_hi', 'crop_name_en', 'icon', 'season', 'sowing_time', 
        'summary', 'soil_preparation', 'fertilizer_schedule', 'irrigation_info', 
        'pest_management_tips', 'image', 'is_featured', 'is_active', 'display_order', 'slug'
    )

    def icon_badge(self, obj):
        return format_html('<span style="font-size: 1.4rem;">{}</span>', obj.icon)
    icon_badge.short_description = "आइकन"


@admin.register(FarmerTip)
class FarmerTipAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category_badge', 'published_date', 
        'is_published', 'is_featured', 'display_order'
    )
    list_filter = ('category', 'is_published', 'is_featured', 'published_date')
    search_fields = ('title', 'summary', 'content')
    list_editable = ('is_published', 'is_featured', 'display_order')
    fields = (
        'title', 'category', 'summary', 'content', 'safety_note', 
        'featured_image', 'published_date', 'is_published', 'is_featured', 'display_order', 'slug'
    )

    def category_badge(self, obj):
        return obj.get_category_display().split(' (')[0]
    category_badge.short_description = "सलाह श्रेणी"
