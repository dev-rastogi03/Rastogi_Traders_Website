from django.test import TestCase, Client
from django.urls import reverse
from products.models import Category, Product


class ProductsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.cat = Category.objects.create(
            name_hi="उर्वरक",
            name_en="Fertilizers",
            slug="fertilizers",
            icon="🌾",
            short_description="सभी प्रकार के उर्वरक"
        )
        self.product = Product.objects.create(
            category=self.cat,
            name="इफको डीएपी 18-46-0",
            slug="iffco-dap-18-46-0",
            brand="IFFCO",
            pack_size="50 kg",
            short_description="उत्तम फास्फेटिक उर्वरक",
            availability_status='in_stock'
        )

    def test_product_list_view(self):
        response = self.client.get(reverse('products:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "इफको डीएपी 18-46-0")

    def test_product_search(self):
        response = self.client.get(reverse('products:list'), {'q': 'डीएपी'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "इफको डीएपी 18-46-0")

    def test_category_view(self):
        response = self.client.get(reverse('products:category', kwargs={'slug': self.cat.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "उर्वरक")
        self.assertContains(response, "इफको डीएपी 18-46-0")

    def test_product_detail_view(self):
        response = self.client.get(reverse('products:detail', kwargs={'slug': self.product.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "इफको डीएपी 18-46-0")
        self.assertContains(response, "सुरक्षा निर्देश")
        self.assertContains(response, "WhatsApp पर लें")

    def test_admin_product_changelist_and_add(self):
        from django.contrib.auth.models import User
        admin_user = User.objects.create_superuser(username='testadmin', password='testpassword123', email='test@test.com')
        self.client.login(username='testadmin', password='testpassword123')
        
        # Test changelist page
        changelist_resp = self.client.get('/admin/products/product/')
        self.assertEqual(changelist_resp.status_code, 200)
        self.assertContains(changelist_resp, "इफको डीएपी 18-46-0")

        # Test add product page GET
        add_get_resp = self.client.get('/admin/products/product/add/')
        self.assertEqual(add_get_resp.status_code, 200)

        # Test adding product POST in Hindi
        add_post_resp = self.client.post('/admin/products/product/add/', {
            'name': 'नीम यूरिया सुपर',
            'category': str(self.cat.id),
            'brand': 'इफको',
            'pack_size': '45 kg',
            'availability_status': 'in_stock',
            'price_label': 'आज का भाव पूछें',
            'display_order': '0',
            'short_description': 'उच्च गुणवत्ता यूरिया',
        })
        self.assertEqual(add_post_resp.status_code, 302)
        self.assertTrue(Product.objects.filter(name='नीम यूरिया सुपर').exists())
