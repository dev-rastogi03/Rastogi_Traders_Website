from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Category, Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        qs = Product.objects.select_related('category').all()
        q = self.request.GET.get('q')
        cat_slug = self.request.GET.get('category')
        availability = self.request.GET.get('status')

        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(brand__icontains=q) |
                Q(short_description__icontains=q) |
                Q(suitable_crops__icontains=q)
            )
        if cat_slug:
            qs = qs.filter(category__slug=cat_slug)
        if availability:
            qs = qs.filter(availability_status=availability)

        return qs.order_by('display_order', '-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_active=True).order_by('display_order', 'id')
        context['selected_category'] = self.request.GET.get('category', '')
        context['search_query'] = self.request.GET.get('q', '')
        context['selected_status'] = self.request.GET.get('status', '')
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'products/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object
        context['products'] = category.products.all().order_by('display_order', '-id')
        context['other_categories'] = Category.objects.filter(is_active=True).exclude(id=category.id)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        context['related_products'] = Product.objects.filter(
            category=product.category
        ).exclude(id=product.id)[:4]
        return context
