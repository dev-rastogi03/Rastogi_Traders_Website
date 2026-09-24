import time
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.cache import cache
from django.views.generic import View, TemplateView
from .models import BusinessProfile, Offer, Review, GalleryImage, ContactMessage
from .forms import ContactForm
from products.models import Category, Product
from farmers.models import CropGuide, FarmerTip


def is_rate_limited(request, action='contact', max_requests=5, window_seconds=600):
    """
    Lightweight rate limiter using client IP.
    Allows up to `max_requests` within `window_seconds` (default 5 requests per 10 mins).
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR', '127.0.0.1')

    cache_key = f"rl_{action}_{ip}"
    current_timestamps = cache.get(cache_key, [])
    now = time.time()

    valid_timestamps = [t for t in current_timestamps if now - t < window_seconds]

    if len(valid_timestamps) >= max_requests:
        return True

    valid_timestamps.append(now)
    cache.set(cache_key, valid_timestamps, timeout=window_seconds)
    return False


class HomeView(View):
    def get(self, request):
        categories = Category.objects.filter(is_active=True).order_by('display_order', 'id')
        featured_products = Product.objects.filter(is_featured=True).select_related('category')[:8]
        if not featured_products.exists():
            featured_products = Product.objects.all().select_related('category')[:8]

        active_offers = Offer.objects.filter(is_active=True).order_by('display_order', '-created_at')[:4]
        crop_guides = CropGuide.objects.filter(is_active=True, is_featured=True).order_by('display_order', 'id')[:6]
        recent_tips = FarmerTip.objects.filter(is_published=True).order_by('display_order', '-published_date')[:3]
        approved_reviews = Review.objects.filter(is_approved=True).order_by('display_order', '-created_at')[:6]
        gallery_images = GalleryImage.objects.filter(is_featured=True).order_by('display_order', '-created_at')[:6]
        if not gallery_images.exists():
            gallery_images = GalleryImage.objects.all().order_by('display_order', '-created_at')[:6]

        form = ContactForm()

        context = {
            'categories': categories,
            'featured_products': featured_products,
            'active_offers': active_offers,
            'crop_guides': crop_guides,
            'recent_tips': recent_tips,
            'reviews': approved_reviews,
            'gallery_images': gallery_images,
            'contact_form': form,
        }
        return render(request, 'core/index.html', context)

    def post(self, request):
        if is_rate_limited(request, action='home_contact', max_requests=5, window_seconds=600):
            messages.error(request, "सुरक्षा चेतावनी: आपने हाल ही में कई संदेश भेजे हैं। कृपया 10 मिनट बाद पुनः प्रयास करें या सीधे कॉल करें।")
            return redirect('core:home')

        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "धन्यवाद! आपका संदेश सफलतापूर्वक भेज दिया गया है। हम शीघ्र ही आपसे संपर्क करेंगे।")
            return redirect('core:home')
        else:
            first_error = next(iter(form.errors.values()))[0] if form.errors else "कृपया फॉर्म में सही जानकारी भरें।"
            messages.error(request, f"त्रुटि: {first_error}")
            return redirect('core:home')


class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['reviews'] = Review.objects.filter(is_approved=True).order_by('display_order', '-created_at')[:4]
        ctx['gallery_preview'] = GalleryImage.objects.all()[:4]
        return ctx


class OffersView(TemplateView):
    template_name = 'core/offers.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['offers'] = Offer.objects.filter(is_active=True).order_by('display_order', '-created_at')
        return ctx


class GalleryView(TemplateView):
    template_name = 'core/gallery.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        category_filter = self.request.GET.get('cat', 'all')
        if category_filter and category_filter != 'all':
            images = GalleryImage.objects.filter(category=category_filter).order_by('display_order', '-created_at')
        else:
            images = GalleryImage.objects.all().order_by('display_order', '-created_at')
        
        ctx['gallery_images'] = images
        ctx['current_cat'] = category_filter
        ctx['categories'] = GalleryImage.CATEGORY_CHOICES
        return ctx


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'core/contact.html', {'form': form})

    def post(self, request):
        if is_rate_limited(request, action='page_contact', max_requests=5, window_seconds=600):
            messages.error(request, "सुरक्षा चेतावनी: आपने हाल ही में कई संदेश भेजे हैं। कृपया 10 मिनट बाद पुनः प्रयास करें या सीधे दिए गए नंबर पर फोन करें।")
            return redirect('core:contact')

        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "धन्यवाद! आपकी पूछताछ रस्तोगी ट्रेडर्स को प्राप्त हो गई है। हमारी टीम जल्द ही आपसे फोन पर संपर्क करेगी।")
            return redirect('core:contact')
        else:
            first_error = next(iter(form.errors.values()))[0] if form.errors else "कृपया फॉर्म में सही जानकारी भरें।"
            messages.error(request, f"त्रुटि: {first_error}")
        return render(request, 'core/contact.html', {'form': form})


class PrivacyPolicyView(TemplateView):
    template_name = 'core/privacy_policy.html'


class TermsConditionsView(TemplateView):
    template_name = 'core/terms_conditions.html'


class CookiesPolicyView(TemplateView):
    template_name = 'core/cookies_policy.html'


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Allow: /",
        "Sitemap: " + request.build_absolute_uri('/sitemap.xml'),
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)


def custom_500_view(request):
    return render(request, '500.html', status=500)
