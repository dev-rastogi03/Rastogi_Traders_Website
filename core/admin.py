from django.contrib import admin
from django.utils.html import format_html
from .models import BusinessProfile, Offer, Review, GalleryImage, ContactMessage

# Custom Admin Site Header & Titles
admin.site.site_header = "रस्तोगी ट्रेडर्स एडमिन पैनल (Rastogi Traders Admin)"
admin.site.site_title = "Rastogi Traders Portal"
admin.site.index_title = "वेबसाइट सामग्री प्रबंधन (Website Content Management)"


@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ("मूल जानकारी एवं संपर्क (Basic Info & Contact)", {
            "fields": (
                "business_name", "tagline", "owner_name", 
                "phone_primary", "phone_secondary", "whatsapp_number", "email"
            )
        }),
        ("दुकान का पता व समय (Address & Hours)", {
            "fields": (
                "address", "landmark", "city_district", "state_pincode", 
                "opening_hours", "sunday_hours"
            )
        }),
        ("गूगल मैप्स लोकेशन (Google Maps Settings)", {
            "fields": (
                "google_maps_directions_url", "google_maps_embed_url"
            ),
            "description": "यहाँ अपने गूगल मैप्स का लिंक और एम्बेड कोड अपडेट करें।"
        }),
        ("हीरो सेक्शन व विवरण (Hero Section & About Story)", {
            "fields": (
                "hero_subtitle", "hero_supporting_text", "about_short_text", "about_story",
                "logo", "hero_banner"
            )
        }),
        ("दुकान संचालक एवं प्रबंधक (Leadership & Owners)", {
            "fields": (
                ("owner_1_name", "owner_1_role"),
                ("owner_1_desc", "owner_1_photo"),
                ("owner_2_name", "owner_2_role"),
                ("owner_2_desc", "owner_2_photo"),
            ),
            "description": "यहाँ दुकान के दोनों संचालकों/मालिकों की फोटो, नाम और पद जोड़ें व अपडेट करें।"
        }),
        ("भरोसा बिंदु (Trust Highlights)", {
            "fields": (
                ("trust_point_1_title", "trust_point_1_desc"),
                ("trust_point_2_title", "trust_point_2_desc"),
                ("trust_point_3_title", "trust_point_3_desc"),
                ("trust_point_4_title", "trust_point_4_desc"),
            ),
            "classes": ("collapse",)
        }),
        ("सोशल मीडिया लिंक्स (Social Media - Optional)", {
            "fields": ("facebook_url", "instagram_url", "youtube_url"),
            "classes": ("collapse",)
        }),
        ("वेबसाइट डेवलपर क्रेडिट (Website Developer Credits)", {
            "fields": (
                "developer_credit_enabled",
                ("developer_credit_name", "developer_credit_role"),
                "developer_credit_url",
            ),
            "description": "यहाँ से आप फुटर में प्रदर्शित होने वाले वेबसाइट डेवलपर का नाम, टाइटल और पोर्टफोलियो/सोशल लिंक आसानी से बदल सकते हैं।"
        }),
    )

    def has_add_permission(self, request):
        # Allow only 1 BusinessProfile instance (Singleton)
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'badge_text', 'deal_highlight', 'valid_from', 'valid_until', 'is_active', 'display_order', 'image_preview')
    list_filter = ('is_active', 'valid_from')
    search_fields = ('title', 'description', 'deal_highlight')
    list_editable = ('is_active', 'display_order')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 35px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "फोटो नहीं"
    image_preview.short_description = "फोटो"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'village_location', 'rating_stars', 'is_approved', 'display_order', 'created_at')
    list_filter = ('is_approved', 'rating', 'created_at')
    search_fields = ('customer_name', 'village_location', 'review_text')
    list_editable = ('is_approved', 'display_order')

    def rating_stars(self, obj):
        return "★" * obj.rating
    rating_stars.short_description = "रेटिंग"


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'display_order', 'image_preview', 'created_at')
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'caption')
    list_editable = ('is_featured', 'display_order')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 60px; height: 40px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "फोटो"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'village', 'interested_category', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'phone', 'village', 'message')
    list_editable = ('is_read',)
    readonly_fields = ('created_at',)
