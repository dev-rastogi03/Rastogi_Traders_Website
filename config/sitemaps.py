from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product, Category
from farmers.models import CropGuide, FarmerTip


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'weekly'

    def items(self):
        return ['core:home', 'core:about', 'core:offers', 'core:gallery', 'core:contact', 'products:list', 'farmers:index']

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return Product.objects.all()




class CategorySitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return Category.objects.filter(is_active=True)


class CropGuideSitemap(Sitemap):
    priority = 0.7
    changefreq = 'monthly'

    def items(self):
        return CropGuide.objects.filter(is_active=True)


class FarmerTipSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        return FarmerTip.objects.filter(is_published=True)
