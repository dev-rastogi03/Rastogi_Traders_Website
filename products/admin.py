from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('icon_badge', 'name_hi', 'name_en', 'products_count', 'display_order', 'is_active')
    list_editable = ('display_order', 'is_active')
    search_fields = ('name_hi', 'name_en', 'short_description')
    fields = ('name_hi', 'name_en', 'icon', 'short_description', 'badge_text', 'image', 'display_order', 'is_active', 'slug')

    def icon_badge(self, obj):
        return format_html('<span style="font-size: 1.4rem;">{}</span>', obj.icon)
    icon_badge.short_description = "आइकन"

    def products_count(self, obj):
        return obj.products.count()
    products_count.short_description = "कुल उत्पाद"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'image_thumbnail', 'name', 'category', 'brand', 
        'pack_size', 'availability_status', 'is_featured', 'display_order'
    )
    list_filter = ('category', 'availability_status', 'is_featured', 'brand')
    search_fields = ('name', 'brand', 'short_description', 'detailed_description', 'suitable_crops')
    list_editable = ('availability_status', 'is_featured', 'display_order')
    list_per_page = 20

    fieldsets = (
        ("उत्पाद मूल विवरण (Basic Product Info)", {
            "fields": ("name", "category", "brand", "pack_size", "image")
        }),
        ("उपलब्धता एवं मूल्य (Stock Status & Price)", {
            "fields": (
                "availability_status", "is_featured", "price_label", "price", "display_order"
            )
        }),
        ("हिंदी विवरण एवं फसलें (Description & Crops)", {
            "fields": ("short_description", "suitable_crops", "detailed_description")
        }),
        ("उन्नत एवं सुरक्षा सेटिंग्स (Advanced & Safety)", {
            "fields": ("slug", "safety_precaution"),
            "classes": ("collapse",),
            "description": "Slug खाली छोड़ने पर उत्पाद के नाम से अपने आप बन जाएगा।"
        }),
    )

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: contain; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 2px;" />', obj.image.url)
        return format_html('<span style="color: #94a3b8; font-size: 0.85rem;">{}</span>', '[फोटो नहीं]')
    image_thumbnail.short_description = "फोटो"
