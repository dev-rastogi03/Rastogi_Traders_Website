import urllib.parse
from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag(takes_context=True)
def whatsapp_product_link(context, product):
    """
    Generates a WhatsApp click-to-chat URL specific to a product.
    Format: नमस्ते, मुझे [PRODUCT NAME] ([BRAND]) की कीमत और उपलब्धता के बारे में जानकारी चाहिए।
    """
    profile = context.get('profile')
    if profile and profile.clean_whatsapp_number:
        number = profile.clean_whatsapp_number
    else:
        number = getattr(settings, 'DEFAULT_WHATSAPP_NUMBER', '+919876543210').replace('+', '').replace(' ', '')

    msg = f"नमस्ते, मुझे Rastogi Traders से '{product.name} ({product.brand})' की कीमत (आज का भाव) और उपलब्धता के बारे में जानकारी चाहिए।"
    encoded = urllib.parse.quote(msg)
    return f"https://wa.me/{number}?text={encoded}"


@register.simple_tag(takes_context=True)
def whatsapp_offer_link(context, offer):
    """
    Generates a WhatsApp click-to-chat URL for a specific offer.
    """
    profile = context.get('profile')
    if profile and profile.clean_whatsapp_number:
        number = profile.clean_whatsapp_number
    else:
        number = getattr(settings, 'DEFAULT_WHATSAPP_NUMBER', '+919876543210').replace('+', '').replace(' ', '')

    msg = f"नमस्ते, मुझे आज के खास ऑफर '{offer.title}' के बारे में जानकारी और आज का भाव चाहिए।"
    encoded = urllib.parse.quote(msg)
    return f"https://wa.me/{number}?text={encoded}"


@register.simple_tag(takes_context=True)
def whatsapp_crop_link(context, crop):
    """
    Generates a WhatsApp click-to-chat URL for crop advice.
    """
    profile = context.get('profile')
    if profile and profile.clean_whatsapp_number:
        number = profile.clean_whatsapp_number
    else:
        number = getattr(settings, 'DEFAULT_WHATSAPP_NUMBER', '+919876543210').replace('+', '').replace(' ', '')

    msg = f"नमस्ते, मुझे '{crop.crop_name_hi}' की फसल के लिए उपयुक्त खाद एवं फसल सुरक्षा उत्पादों के बारे में परामर्श चाहिए।"
    encoded = urllib.parse.quote(msg)
    return f"https://wa.me/{number}?text={encoded}"


@register.simple_tag(takes_context=True)
def whatsapp_custom_link(context, custom_text):
    """
    Generates a WhatsApp URL with any custom message.
    """
    profile = context.get('profile')
    if profile and profile.clean_whatsapp_number:
        number = profile.clean_whatsapp_number
    else:
        number = getattr(settings, 'DEFAULT_WHATSAPP_NUMBER', '+919876543210').replace('+', '').replace(' ', '')

    encoded = urllib.parse.quote(custom_text)
    return f"https://wa.me/{number}?text={encoded}"


@register.filter
def star_range(value):
    """Returns range for star ratings"""
    try:
        return range(int(value))
    except (ValueError, TypeError):
        return range(5)


@register.filter
def remaining_stars(value):
    """Returns remaining empty stars out of 5"""
    try:
        return range(5 - int(value))
    except (ValueError, TypeError):
        return range(0)
