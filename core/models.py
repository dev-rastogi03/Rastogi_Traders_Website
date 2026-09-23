from django.db import models
from django.utils import timezone


class BusinessProfile(models.Model):
    """
    Singleton model to store business contact info, location, branding, and hero texts.
    Configurable from Django Admin without modifying source code.
    """
    business_name = models.CharField(
        max_length=200, 
        default="Rastogi Traders | रस्तोगी ट्रेडर्स",
        verbose_name="दुकान / व्यवसाय का नाम (Business Name)"
    )
    tagline = models.CharField(
        max_length=255, 
        default="किसानों की खेती का भरोसेमंद साथी",
        verbose_name="मुख्य टैगलाइन (Tagline)"
    )
    hero_subtitle = models.CharField(
        max_length=255, 
        default="उर्वरक • कीटनाशक • पशु आहार",
        verbose_name="हीरो उप-शीर्षक (Hero Subtitle)"
    )
    hero_supporting_text = models.TextField(
        default="खेती और पशुपालन से जुड़े आवश्यक उत्पादों के लिए हमसे संपर्क करें। स्थानीय किसानों का सच्चा साथी।",
        verbose_name="हीरो विवरण (Hero Supporting Text)"
    )
    owner_name = models.CharField(
        max_length=150, 
        default="रस्तोगी परिवार", 
        verbose_name="संचालक का नाम (Owner / Family Name)"
    )
    phone_primary = models.CharField(
        max_length=20, 
        default="+91 9876543210", 
        verbose_name="प्राथमिक फोन नंबर (Primary Call Number)"
    )
    phone_secondary = models.CharField(
        max_length=20, 
        blank=True, 
        verbose_name="अतिरिक्त फोन नंबर (Secondary Phone - Optional)"
    )
    whatsapp_number = models.CharField(
        max_length=20, 
        default="+919876543210", 
        verbose_name="व्हाट्सऐप नंबर (WhatsApp Number with Country Code)"
    )
    email = models.EmailField(
        blank=True, 
        default="info@rastogitraders.in",
        verbose_name="ईमेल (Email Address - Optional)"
    )
    address = models.TextField(
        default="मुख्य बाजार, कृषि सेवा केंद्र के पास, (तहसील / जिला क्षेत्र)",
        verbose_name="दुकान का पूरा पता (Shop Address)"
    )
    landmark = models.CharField(
        max_length=200, 
        blank=True, 
        default="कृषि मंडी रोड के निकट",
        verbose_name="लैंडमार्क / पहचान (Landmark)"
    )
    city_district = models.CharField(
        max_length=100, 
        default="सीतापुर / लखीमपुर क्षेत्र", 
        verbose_name="शहर / जिला (City / District)"
    )
    state_pincode = models.CharField(
        max_length=100, 
        default="उत्तर प्रदेश", 
        verbose_name="राज्य / पिन कोड (State / PIN)"
    )
    opening_hours = models.CharField(
        max_length=200, 
        default="सुबह 8:00 बजे से शाम 8:00 बजे तक (सोमवार - शनिवार)",
        verbose_name="खुलने का समय (Opening Hours)"
    )
    sunday_hours = models.CharField(
        max_length=100, 
        default="रविवार: सुबह 9:00 से दोपहर 2:00 बजे तक", 
        blank=True,
        verbose_name="रविवार का समय (Sunday Hours)"
    )
    google_maps_directions_url = models.URLField(
        max_length=500, 
        blank=True, 
        default="https://maps.google.com/?q=Rastogi+Traders",
        verbose_name="गूगल मैप्स दिशा-निर्देश लिंक (Google Maps Directions Link)"
    )
    google_maps_embed_url = models.TextField(
        blank=True,
        default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d113944.37684877717!2d80.61286884351336!3d27.568478470559196!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3998e3b7b396e9cf%3A0x6b4aa9bece4c5417!2sSitapur%2C%20Uttar%20Pradesh!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin",
        verbose_name="गूगल मैप्स एम्बेड URL (Google Maps Embed Iframe Src)"
    )
    about_story = models.TextField(
        default="Rastogi Traders एक स्थानीय कृषि उत्पाद व्यवसाय है, जहाँ किसानों और पशुपालकों के लिए उर्वरक, फसल सुरक्षा उत्पाद और पशु आहार उपलब्ध कराए जाते हैं। हमारा उद्देश्य ग्राहकों को आवश्यक कृषि उत्पादों की जानकारी और आसान संपर्क सुविधा प्रदान करना है। कई वर्षों के भरोसे और उत्तम सेवा के साथ हम हर किसान की खुशहाली के प्रति समर्पित हैं।",
        verbose_name="हमारे बारे में पूरी कहानी (About Business Story)"
    )
    about_short_text = models.TextField(
        default="उच्च गुणवत्ता वाले कृषि उत्पाद, उचित परामर्श और स्थानीय किसानों का अटूट विश्वास।",
        verbose_name="संक्षिप्त परिचय (About Short Description)"
    )
    
    # Trust points (Editable in Admin)
    trust_point_1_title = models.CharField(max_length=100, default="स्थानीय एवं भरोसेमंद सेवा", verbose_name="भरोसा बिंदु 1 शीर्षक")
    trust_point_1_desc = models.CharField(max_length=255, default="स्थानीय किसानों और ग्राहकों के लिए आसान और विश्वसनीय संपर्क।", verbose_name="भरोसा बिंदु 1 विवरण")
    
    trust_point_2_title = models.CharField(max_length=100, default="विभिन्न कृषि उत्पाद", verbose_name="भरोसा बिंदु 2 शीर्षक")
    trust_point_2_desc = models.CharField(max_length=255, default="उर्वरक, फसल सुरक्षा उत्पाद (कीटनाशक) और पौष्टिक पशु आहार एक ही छत के नीचे।", verbose_name="भरोसा बिंदु 2 विवरण")
    
    trust_point_3_title = models.CharField(max_length=100, default="आसान संपर्क सुविधा", verbose_name="भरोसा बिंदु 3 शीर्षक")
    trust_point_3_desc = models.CharField(max_length=255, default="फोन और WhatsApp के माध्यम से आज का भाव और उत्पाद उपलब्धता तुरंत जानें।", verbose_name="भरोसा बिंदु 3 विवरण")
    
    trust_point_4_title = models.CharField(max_length=100, default="दुकान पर सीधी उपलब्धता", verbose_name="भरोसा बिंदु 4 शीर्षक")
    trust_point_4_desc = models.CharField(max_length=255, default="असली और ब्रांडेड कंपनियों के स्टॉक की दुकान पर सीधी जाँच और खरीद।", verbose_name="भरोसा बिंदु 4 विवरण")

    # Leadership / Owners Section (About Us page)
    owner_1_name = models.CharField(
        max_length=120, 
        default="श्री रमेश रस्तोगी", 
        verbose_name="स्वामी / मुख्य संचालक का नाम (Owner 1 Name)"
    )
    owner_1_role = models.CharField(
        max_length=100, 
        default="संस्थापक एवं मुख्य संचालक (Founder & Proprietor)", 
        verbose_name="पद / दायित्व (Owner 1 Role)"
    )
    owner_1_desc = models.CharField(
        max_length=255, 
        default="कृषि व्यापार एवं बीज-खाद परामर्श में 25+ वर्षों का अटूट अनुभव।", 
        verbose_name="संक्षिप्त परिचय (Owner 1 Bio / Description)"
    )
    owner_1_photo = models.ImageField(
        upload_to="profile/team/", 
        blank=True, 
        null=True, 
        verbose_name="स्वामी की फोटो (Owner 1 Photo)"
    )

    owner_2_name = models.CharField(
        max_length=120, 
        default="श्री अमित रस्तोगी", 
        verbose_name="प्रबंधक / सह-संचालक का नाम (Owner 2 / Manager Name)"
    )
    owner_2_role = models.CharField(
        max_length=100, 
        default="प्रबंधक एवं ग्राहक सेवा प्रमुख (Store Manager)", 
        verbose_name="पद / दायित्व (Owner 2 / Manager Role)"
    )
    owner_2_desc = models.CharField(
        max_length=255, 
        default="उत्पाद उपलब्धता, स्टॉक प्रबंधन एवं किसान बंधुओं को त्वरित सेवा।", 
        verbose_name="संक्षिप्त परिचय (Owner 2 Bio / Description)"
    )
    owner_2_photo = models.ImageField(
        upload_to="profile/team/", 
        blank=True, 
        null=True, 
        verbose_name="प्रबंधक की फोटो (Owner 2 / Manager Photo)"
    )

    # Social links (optional)
    facebook_url = models.URLField(blank=True, verbose_name="फेसबुक लिंक (Facebook URL)")
    instagram_url = models.URLField(blank=True, verbose_name="इंस्टाग्राम लिंक (Instagram URL)")
    youtube_url = models.URLField(blank=True, verbose_name="यूट्यूब लिंक (YouTube URL)")

    logo = models.ImageField(upload_to="profile/", blank=True, null=True, verbose_name="दुकान का लोगो (Logo)")
    hero_banner = models.ImageField(upload_to="profile/", blank=True, null=True, verbose_name="हीरो बैनर फोटो (Hero Banner Image)")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "दुकान की जानकारी (Business Profile)"
        verbose_name_plural = "दुकान की जानकारी (Business Profile)"

    def __str__(self):
        return self.business_name

    @classmethod
    def get_solo(cls):
        obj, created = cls.objects.get_or_create(id=1)
        return obj

    @property
    def clean_whatsapp_number(self):
        """Returns clean digits with country code for wa.me links"""
        return ''.join(filter(str.isdigit, self.whatsapp_number))

    @property
    def clean_phone_primary(self):
        """Returns clean digits for tel: links"""
        return ''.join(filter(str.isdigit, self.phone_primary))


class Offer(models.Model):
    """Seasonal offers and promotions managed from admin"""
    title = models.CharField(max_length=200, verbose_name="ऑफर का नाम (Offer Title)")
    badge_text = models.CharField(max_length=80, default="सीमित समय ऑफर", verbose_name="बैज टेक्स्ट (Badge Text)")
    description = models.TextField(verbose_name="ऑफर का विवरण (Description)")
    deal_highlight = models.CharField(max_length=150, blank=True, verbose_name="मुख्य लाभ / बचत (Deal Highlight e.g. आज का विशेष भाव)")
    image = models.ImageField(upload_to="offers/", blank=True, null=True, verbose_name="ऑफर फोटो (Offer Image)")
    valid_from = models.DateField(default=timezone.now, verbose_name="शुरुआत तिथि (Valid From)")
    valid_until = models.DateField(blank=True, null=True, verbose_name="अंतिम तिथि (Valid Until - Optional)")
    is_active = models.BooleanField(default=True, verbose_name="सक्रिय है? (Is Active)")
    display_order = models.PositiveIntegerField(default=0, verbose_name="क्रम संख्या (Display Order)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "ऑफर (Offer)"
        verbose_name_plural = "आज के खास ऑफर (Special Offers)"
        ordering = ['display_order', '-created_at']

    def __str__(self):
        return self.title


class Review(models.Model):
    """Customer testimonials and feedback"""
    RATING_CHOICES = [(i, f"{i} स्टार") for i in range(5, 0, -1)]

    customer_name = models.CharField(max_length=150, verbose_name="किसान / ग्राहक का नाम (Customer Name)")
    village_location = models.CharField(max_length=150, verbose_name="गाँव / कस्बा (Village / Town)")
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5, verbose_name="रेटिंग (Rating)")
    review_text = models.TextField(verbose_name="ग्राहक की राय / अनुभव (Review Text)")
    customer_photo = models.ImageField(upload_to="reviews/", blank=True, null=True, verbose_name="फोटो (Photo - Optional)")
    is_approved = models.BooleanField(default=True, verbose_name="स्वीकृत / प्रदर्शित करें (Is Approved)")
    display_order = models.PositiveIntegerField(default=0, verbose_name="क्रम (Display Order)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="दिनांक (Created At)")

    class Meta:
        verbose_name = "ग्राहक समीक्षा (Customer Review)"
        verbose_name_plural = "ग्राहकों की राय (Customer Reviews)"
        ordering = ['display_order', '-created_at']

    def __str__(self):
        return f"{self.customer_name} ({self.village_location}) - {self.rating}★"


class GalleryImage(models.Model):
    """Photos of shop, stock, and local agriculture"""
    CATEGORY_CHOICES = [
        ('shop', 'दुकान व काउंटर (Shop & Counter)'),
        ('stock', 'उर्वरक एवं बीज स्टॉक (Fertilizers & Seeds Stock)'),
        ('cattle_feed', 'पशु आहार स्टॉक (Cattle Feed Stock)'),
        ('farmers', 'किसान व कृषि परिवेश (Farmers & Fields)'),
    ]

    title = models.CharField(max_length=150, verbose_name="फोटो का शीर्षक (Title)")
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='shop', verbose_name="गैलरी श्रेणी (Category)")
    image = models.ImageField(upload_to="gallery/", verbose_name="तस्वीर (Image File)")
    caption = models.CharField(max_length=255, blank=True, verbose_name="कैप्शन (Caption - Optional)")
    is_featured = models.BooleanField(default=False, verbose_name="मुख्य पृष्ठ पर दिखाएँ (Show on Homepage)")
    display_order = models.PositiveIntegerField(default=0, verbose_name="क्रम (Display Order)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "गैलरी फोटो (Gallery Photo)"
        verbose_name_plural = "दुकान व स्टॉक फोटो गैलरी (Gallery Images)"
        ordering = ['display_order', '-created_at']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """Customer direct enquiries from the contact form"""
    name = models.CharField(max_length=120, verbose_name="नाम (Name)")
    phone = models.CharField(max_length=20, verbose_name="मोबाइल नंबर (Mobile Phone)")
    village = models.CharField(max_length=150, blank=True, verbose_name="गाँव / स्थान (Village / Location)")
    interested_category = models.CharField(max_length=100, blank=True, verbose_name="रुचि का विषय / उत्पाद (Interested In)")
    message = models.TextField(verbose_name="संदेश / पूछताछ (Message)")
    is_read = models.BooleanField(default=False, verbose_name="पढ़ा गया (Is Read)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="प्राप्ति समय (Received At)")

    class Meta:
        verbose_name = "पूछताछ संदेश (Contact Enquiry)"
        verbose_name_plural = "वेबसाइट पूछताछ संदेश (Customer Enquiries)"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.phone} ({self.created_at.strftime('%d-%b-%Y')})"
