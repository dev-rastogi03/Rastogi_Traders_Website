import urllib.parse
from django.conf import settings
from .models import BusinessProfile
from products.models import Category


def global_site_context(request):
    """
    Globally exposes business profile, navigation categories, and pre-built contact links
    to every template in the application.
    """
    try:
        profile = BusinessProfile.get_solo()
    except Exception:
        profile = None

    categories = Category.objects.filter(is_active=True).order_by('display_order', 'id')

    # Pre-generate general WhatsApp URL
    whatsapp_number = profile.clean_whatsapp_number if profile else settings.DEFAULT_WHATSAPP_NUMBER.replace('+', '').replace(' ', '')
    default_msg = "नमस्ते, मुझे Rastogi Traders के कृषि उत्पादों (खाद, बीज, कीटनाशक, पशु आहार) के बारे में जानकारी चाहिए।"
    encoded_msg = urllib.parse.quote(default_msg)
    whatsapp_general_url = f"https://wa.me/{whatsapp_number}?text={encoded_msg}"

    # Pre-generate phone call link
    primary_phone = profile.clean_phone_primary if profile else settings.DEFAULT_BUSINESS_PHONE.replace(' ', '')
    phone_call_url = f"tel:{primary_phone}"

    return {
        'profile': profile,
        'global_categories': categories,
        'whatsapp_general_url': whatsapp_general_url,
        'phone_call_url': phone_call_url,
    }
