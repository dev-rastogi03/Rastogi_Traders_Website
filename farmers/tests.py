from django.test import TestCase, Client
from django.urls import reverse
from farmers.models import CropGuide, FarmerTip


class FarmersTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.crop = CropGuide.objects.create(
            crop_name_hi="गेहूँ (Wheat)",
            crop_name_en="Wheat",
            slug="wheat-gehun",
            icon="🌾",
            season="रबी सीजन",
            summary="गेहूँ की उन्नत खेती के उपाय"
        )
        self.tip = FarmerTip.objects.create(
            title="गेहूँ की फसल में कल्ले फूटते समय खाद",
            slug="wheat-tillering-tips",
            category="soil_fertilizer",
            summary="समय पर सिंचाई और यूरिया+जिंक का संतुलित प्रयोग",
            content="विस्तृत विवरण...",
            is_published=True
        )

    def test_farmer_corner_index(self):
        response = self.client.get(reverse('farmers:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "गेहूँ (Wheat)")
        self.assertContains(response, "किसान कॉर्नर")

    def test_crop_detail_view(self):
        response = self.client.get(reverse('farmers:crop_detail', kwargs={'slug': self.crop.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "गेहूँ (Wheat)")
        self.assertContains(response, "रबी सीजन")

    def test_farmer_tip_detail_view(self):
        response = self.client.get(reverse('farmers:tip_detail', kwargs={'slug': self.tip.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "गेहूँ की फसल में कल्ले फूटते समय खाद")
