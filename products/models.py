import uuid
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def generate_unique_slug(model_instance, text, default_prefix='item'):
    """
    Generates a unique, safe slug for Hindi/English names with fallback.
    """
    if not text:
        text = f"{default_prefix}-{uuid.uuid4().hex[:6]}"
    
    slug = slugify(text, allow_unicode=True)
    if not slug or slug.strip() == "":
        slug = slugify(text) or f"{default_prefix}-{uuid.uuid4().hex[:6]}"
    
    unique_slug = slug
    counter = 1
    model_class = model_instance.__class__
    while model_class.objects.filter(slug=unique_slug).exclude(pk=model_instance.pk).exists():
        unique_slug = f"{slug}-{counter}"
        counter += 1
    return unique_slug


class Category(models.Model):
    """
    Product categories e.g. Fertilizers, Pesticides, Cattle Feed, Seeds.
    Manageable from Django Admin.
    """
    name_hi = models.CharField(
        max_length=150, 
        verbose_name="श्रेणी का नाम - हिंदी (Category Hindi Name)"
    )
    name_en = models.CharField(
        max_length=150, 
        blank=True,
        verbose_name="Category English Name"
    )
    slug = models.SlugField(
        max_length=150, 
        unique=True, 
        blank=True,
        help_text="URL Identifier e.g. fertilizers, pesticides, cattle-feed (खाली छोड़ने पर स्वतः बनेगा)"
    )
    icon = models.CharField(
        max_length=30, 
        default="🌾", 
        blank=True,
        verbose_name="आइकन इमोजी / संकेत (Emoji Icon e.g. 🌾, 🌱, 🐄, 🌻)"
    )
    short_description = models.TextField(
        blank=True,
        default="",
        verbose_name="संक्षिप्त विवरण (Short Description in Hindi)"
    )
    badge_text = models.CharField(
        max_length=50, 
        default="सर्वोत्तम गुणवत्ता", 
        blank=True,
        verbose_name="बैज टैग (Badge Text)"
    )
    image = models.ImageField(
        upload_to="categories/", 
        blank=True, 
        null=True,
        verbose_name="श्रेणी फोटो (Category Image)"
    )
    display_order = models.PositiveIntegerField(
        default=0, 
        verbose_name="क्रम संख्या (Display Order)"
    )
    is_active = models.BooleanField(
        default=True, 
        verbose_name="सक्रिय है? (Is Active)"
    )

    class Meta:
        verbose_name = "उत्पाद श्रेणी (Product Category)"
        verbose_name_plural = "उत्पाद श्रेणियाँ (Product Categories)"
        ordering = ['display_order', 'id']

    def __str__(self):
        return f"{self.icon} {self.name_hi}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.name_en or self.name_hi, default_prefix='category')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:category', kwargs={'slug': self.slug})


class Product(models.Model):
    """
    Agricultural product model.
    Focus on WhatsApp Enquiry, Availability status, Pack size, and Safety.
    """
    AVAILABILITY_CHOICES = [
        ('in_stock', 'दुकान पर उपलब्ध (In Stock)'),
        ('limited_stock', 'सीमित स्टॉक (Limited Stock)'),
        ('on_order', 'ऑर्डर पर उपलब्ध (Available on Order)'),
        ('out_of_stock', 'वर्तमान में अनुपलब्ध (Out of Stock)'),
    ]

    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="products", 
        verbose_name="श्रेणी (Category)"
    )
    name = models.CharField(
        max_length=200, 
        verbose_name="उत्पाद का नाम (Product Name)"
    )
    slug = models.SlugField(
        max_length=220, 
        unique=True, 
        blank=True,
        help_text="URL identifier (खाली छोड़ने पर स्वतः बनेगा)"
    )
    brand = models.CharField(
        max_length=150, 
        default="विश्वसनीय ब्रांड", 
        blank=True,
        verbose_name="कंपनी / ब्रांड (Brand / Manufacturer)"
    )
    pack_size = models.CharField(
        max_length=100, 
        default="50 kg / 1 Ltr / 500 gm", 
        blank=True,
        verbose_name="पैकिंग साइज (Pack Size / Unit)"
    )
    short_description = models.TextField(
        blank=True,
        default="",
        verbose_name="संक्षिप्त परिचय (Short Description in Hindi)"
    )
    detailed_description = models.TextField(
        blank=True, 
        verbose_name="विस्तृत विवरण एवं उपयोग (Detailed Information)"
    )
    suitable_crops = models.CharField(
        max_length=255, 
        blank=True, 
        default="गेहूँ, धान, गन्ना, मक्का, आलू, सरसों एवं अन्य फसलें",
        verbose_name="उपयुक्त फसलें (Suitable Crops)"
    )
    image = models.ImageField(
        upload_to="products/", 
        blank=True, 
        null=True,
        verbose_name="उत्पाद फोटो (Product Image)"
    )
    availability_status = models.CharField(
        max_length=30, 
        choices=AVAILABILITY_CHOICES, 
        default='in_stock', 
        verbose_name="उपलब्धता स्थिति (Availability Status)"
    )
    is_featured = models.BooleanField(
        default=False, 
        verbose_name="मुख्य पृष्ठ पर दिखाएँ (Featured on Homepage)"
    )
    price_label = models.CharField(
        max_length=80, 
        default="आज का भाव पूछें", 
        blank=True,
        verbose_name="भाव लेबल (Price Tag Label)"
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True, 
        verbose_name="वैकल्पिक निश्चित मूल्य ₹ (Optional Fixed Price)"
    )
    safety_precaution = models.TextField(
        default="उत्पाद के पैकेट/लेबल पर दिए निर्देशों का पालन करें और आवश्यकता होने पर कृषि विशेषज्ञ से सलाह लें।",
        blank=True,
        verbose_name="सुरक्षा निर्देश एवं वैधानिक चेतावनी (Safety Precautions)"
    )
    display_order = models.PositiveIntegerField(
        default=0, 
        verbose_name="क्रम संख्या (Display Order)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "उत्पाद (Product)"
        verbose_name_plural = "सभी उत्पाद (All Products)"
        ordering = ['display_order', '-id']

    def __str__(self):
        return f"{self.name} ({self.brand}) - {self.get_availability_status_display()}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.name, default_prefix='product')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

    @property
    def is_available(self):
        return self.availability_status in ['in_stock', 'limited_stock']

    @property
    def whatsapp_message(self):
        """Constructs WhatsApp enquiry message in simple Hindi"""
        return f"नमस्ते, मुझे Rastogi Traders से '{self.name} ({self.brand})' की कीमत और उपलब्धता के बारे में जानकारी चाहिए।"
