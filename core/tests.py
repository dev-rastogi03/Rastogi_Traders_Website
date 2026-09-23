from django.test import TestCase, Client
from django.urls import reverse
from core.models import BusinessProfile, Offer, Review, ContactMessage


class CoreViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile = BusinessProfile.get_solo()
        self.profile.business_name = "Rastogi Traders | रस्तोगी ट्रेडर्स"
        self.profile.save()

    def test_homepage_status(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rastogi Traders")
        self.assertContains(response, "WhatsApp")
        self.assertContains(response, "फोन करें")

    def test_about_page_status(self):
        response = self.client.get(reverse('core:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "हमारे बारे में")

    def test_offers_page_status(self):
        response = self.client.get(reverse('core:offers'))
        self.assertEqual(response.status_code, 200)

    def test_gallery_page_status(self):
        response = self.client.get(reverse('core:gallery'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_get(self):
        response = self.client.get(reverse('core:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "संपर्क करें")

    def test_contact_form_submission(self):
        response = self.client.post(reverse('core:contact'), {
            'name': 'सुरेश कुमार',
            'phone': '9876543210',
            'village': 'गाँव रामपुर',
            'interested_category': 'उर्वरक (Fertilizers)',
            'message': 'डीएपी का आज का भाव क्या है?',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ContactMessage.objects.filter(name='सुरेश कुमार').exists())

    def test_robots_txt(self):
        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, 200)
        self.assertIn("User-agent", response.content.decode())

    def test_sitemap_xml(self):
        response = self.client.get('/sitemap.xml')
        self.assertEqual(response.status_code, 200)
        self.assertIn("urlset", response.content.decode())
