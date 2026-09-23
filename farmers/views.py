from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
from .models import CropGuide, FarmerTip
from products.models import Product


class FarmerCornerIndexView(TemplateView):
    template_name = 'farmers/farmer_corner.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_filter = self.request.GET.get('cat')
        
        tips_qs = FarmerTip.objects.filter(is_published=True)
        if cat_filter:
            tips_qs = tips_qs.filter(category=cat_filter)

        context['crop_guides'] = CropGuide.objects.filter(is_active=True).order_by('display_order', 'id')
        context['tips'] = tips_qs.order_by('display_order', '-published_date')
        context['categories'] = FarmerTip.CATEGORY_CHOICES
        context['selected_cat'] = cat_filter
        return context


class CropGuideDetailView(DetailView):
    model = CropGuide
    template_name = 'farmers/crop_detail.html'
    context_object_name = 'crop'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        crop = self.object
        # Recommended products for this crop
        context['recommended_products'] = Product.objects.filter(
            suitable_crops__icontains=crop.crop_name_hi.split(' ')[0]
        )[:4]
        context['other_crops'] = CropGuide.objects.filter(is_active=True).exclude(id=crop.id)
        return context


class FarmerTipDetailView(DetailView):
    model = FarmerTip
    template_name = 'farmers/tip_detail.html'
    context_object_name = 'tip'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tip = self.object
        context['related_tips'] = FarmerTip.objects.filter(
            category=tip.category, is_published=True
        ).exclude(id=tip.id)[:3]
        return context
