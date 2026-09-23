import uuid
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from products.models import generate_unique_slug


class CropGuide(models.Model):
    """
    Detailed agronomy guidance for prominent local Indian crops
    (गेहूँ, धान, मक्का, आलू, गन्ना, सरसों, आदि).
    """
    crop_name_hi = models.CharField(
        max_length=150, 
        verbose_name="फसल का नाम - हिंदी (Crop Hindi Name)"
    )
    crop_name_en = models.CharField(
        max_length=100, 
        blank=True, 
        verbose_name="Crop English Name"
    )
    slug = models.SlugField(
        max_length=150, 
        unique=True, 
        blank=True,
        help_text="URL identifier (खाली छोड़ने पर स्वतः बनेगा)"
    )
    icon = models.CharField(
        max_length=30, 
        default="🌾", 
        verbose_name="इमोजी आइकन (Emoji Icon e.g. 🌾, 🌱, 🌽, 🥔)"
    )
    season = models.CharField(
        max_length=100, 
        default="रबी सीजन (Rabi Season)",
        verbose_name="मौसम / सीजन (Crop Season)"
    )
    sowing_time = models.CharField(
        max_length=120, 
        default="अक्टूबर से दिसंबर",
        verbose_name="बुवाई का उपयुक्त समय (Sowing Time Window)"
    )
    summary = models.TextField(
        verbose_name="संक्षिप्त परिचय (Summary in Simple Hindi)"
    )
    soil_preparation = models.TextField(
        blank=True,
        verbose_name="खेत की तैयारी (Soil Preparation Guidelines)"
    )
    fertilizer_schedule = models.TextField(
        blank=True,
        verbose_name="उर्वरक एवं पोषण सलाह (Fertilizer Management Tips)"
    )
    irrigation_info = models.TextField(
        blank=True,
        verbose_name="सिंचाई प्रबंधन (Irrigation Schedule Stages)"
    )
    pest_management_tips = models.TextField(
        blank=True,
        verbose_name="कीट व रोग नियंत्रण सामान्य सुझाव (Pest & Disease Overview)"
    )
    image = models.ImageField(
        upload_to="crops/", 
        blank=True, 
        null=True, 
        verbose_name="फसल फोटो (Crop Image)"
    )
    is_featured = models.BooleanField(
        default=True, 
        verbose_name="मुख्य पृष्ठ पर दिखाएँ (Show on Home)"
    )
    is_active = models.BooleanField(
        default=True, 
        verbose_name="सक्रिय है? (Is Active)"
    )
    display_order = models.PositiveIntegerField(
        default=0, 
        verbose_name="क्रम (Display Order)"
    )

    class Meta:
        verbose_name = "फसल जानकारी मार्गदर्शिका (Crop Guide)"
        verbose_name_plural = "फसल जानकारी मार्गदर्शिकाएँ (Crop Guides)"
        ordering = ['display_order', 'id']

    def __str__(self):
        return f"{self.icon} {self.crop_name_hi}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.crop_name_en or self.crop_name_hi, default_prefix='crop')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('farmers:crop_detail', kwargs={'slug': self.slug})


class FarmerTip(models.Model):
    """
    Practical agricultural advice articles and dairy feed guidance
    """
    CATEGORY_CHOICES = [
        ('soil_fertilizer', 'उर्वरक एवं पोषण प्रबंधन (Fertilizer & Soil Care)'),
        ('crop_protection', 'फसल सुरक्षा एवं कीट नियंत्रण (Pest Control & Plant Protection)'),
        ('cattle_care', 'पशु आहार एवं डेयरी देखभाल (Cattle Feed & Livestock Care)'),
        ('seasonal_tips', 'मौसम अनुसार खेती के सुझाव (Seasonal Farming Tips)'),
    ]

    title = models.CharField(
        max_length=220, 
        verbose_name="लेख शीर्षक (Article / Tip Title)"
    )
    slug = models.SlugField(
        max_length=250, 
        unique=True, 
        blank=True,
        help_text="URL identifier (खाली छोड़ने पर स्वतः बनेगा)"
    )
    category = models.CharField(
        max_length=40, 
        choices=CATEGORY_CHOICES, 
        default='seasonal_tips', 
        verbose_name="सलाह श्रेणी (Category)"
    )
    summary = models.TextField(
        verbose_name="संक्षिप्त सारांश (Summary)"
    )
    content = models.TextField(
        verbose_name="पूरी जानकारी एवं व्यावहारिक सुझाव (Full Article Content)"
    )
    safety_note = models.TextField(
        default="उत्पाद के पैकेट/लेबल पर दिए निर्देशों का पालन करें और आवश्यकता होने पर नजदीकी कृषि विशेषज्ञ से संपर्क करें।",
        verbose_name="सुरक्षा व वैधानिक सूचना (Safety Note / Disclaimer)"
    )
    featured_image = models.ImageField(
        upload_to="tips/", 
        blank=True, 
        null=True, 
        verbose_name="मुख्य फोटो (Article Photo)"
    )
    published_date = models.DateField(
        default=timezone.now, 
        verbose_name="प्रकाशन तिथि (Published Date)"
    )
    is_published = models.BooleanField(
        default=True, 
        verbose_name="प्रकाशित है? (Is Published)"
    )
    is_featured = models.BooleanField(
        default=False, 
        verbose_name="मुख्य पृष्ठ पर दिखाएँ (Featured on Homepage)"
    )
    display_order = models.PositiveIntegerField(
        default=0, 
        verbose_name="क्रम संख्या (Display Order)"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "कृषि सलाह लेख (Farmer Tip)"
        verbose_name_plural = "किसान सलाह व उपयोगी लेख (Farmer Tips & Articles)"
        ordering = ['display_order', '-published_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.title, default_prefix='tip')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('farmers:tip_detail', kwargs={'slug': self.slug})
