"""
Populates realistic seed data for Rastogi Traders agricultural website.
Includes Business Profile, Categories, Products, Crop Guides, Farmer Tips, Offers, Reviews, and Gallery entries.
"""

import os
import sys
import django

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.files.base import ContentFile
from core.models import BusinessProfile, Offer, Review, GalleryImage
from products.models import Category, Product
from farmers.models import CropGuide, FarmerTip
import datetime


def seed_database():
    print("🌱 Starting Rastogi Traders database seeding...")

    # 1. Business Profile (Singleton)
    profile = BusinessProfile.get_solo()
    profile.business_name = "Rastogi Traders | रस्तोगी ट्रेडर्स"
    profile.tagline = "किसानों की खेती का भरोसेमंद साथी"
    profile.hero_subtitle = "उर्वरक • कीटनाशक • पशु आहार • उन्नत बीज"
    profile.hero_supporting_text = "उच्च गुणवत्ता वाले रासायनिक व जैविक उर्वरक, प्रमाणित कीटनाशक, फसल सुरक्षा दवाइयाँ और पौष्टिक पशु आहार के लिए हमसे सीधे संपर्क करें।"
    profile.owner_name = "रस्तोगी परिवार"
    profile.phone_primary = "+91 9876543210"
    profile.phone_secondary = "+91 9876543211"
    profile.whatsapp_number = "+919876543210"
    profile.email = "contact@rastogitraders.in"
    profile.address = "दुकान नं. 14, मुख्य मंडी रोड, कृषि सेवा केंद्र के सामने"
    profile.landmark = "केंद्रीय बैंक के निकट, अनाज मंडी गेट"
    profile.city_district = "सीतापुर / लखीमपुर परिक्षेत्र"
    profile.state_pincode = "उत्तर प्रदेश - 261001"
    profile.opening_hours = "सुबह 8:00 बजे से शाम 8:00 बजे तक (सोमवार - शनिवार)"
    profile.sunday_hours = "रविवार: सुबह 9:00 बजे से दोपहर 2:00 बजे तक"
    profile.google_maps_directions_url = "https://maps.google.com/?q=Rastogi+Traders+Krishi+Seva"
    profile.google_maps_embed_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d113944.37684877717!2d80.61286884351336!3d27.568478470559196!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3998e3b7b396e9cf%3A0x6b4aa9bece4c5417!2sSitapur%2C%20Uttar%20Pradesh!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin"
    profile.about_story = """Rastogi Traders एक स्थानीय कृषि उत्पाद एवं पशु सेवा प्रतिष्ठान है, जहाँ क्षेत्र के किसान भाइयों और डेयरी पशुपालकों के लिए उच्च गुणवत्ता वाले उर्वरक (खाद), प्रमाणित फसल सुरक्षा उत्पाद (कीटनाशक, फफूंदनाशक), उन्नत बीज और पौष्टिक पशु आहार उपलब्ध कराए जाते हैं।

हमारा मुख्य उद्देश्य हर किसान तक असली और मानक गुणवत्ता वाले उत्पाद पहुँचाना, उन्हें उचित मूल्य पर उपलब्ध कराना और सही उपयोग की सामान्य जानकारी देना है। कई वर्षों के अटूट विश्वास, निष्पक्ष व्यवहार और त्वरित सेवा के दम पर रस्तोगी ट्रेडर्स आज क्षेत्र के हजारों किसानों की पहली पसंद बन चुका है।"""
    profile.about_short_text = "असली खाद, प्रमाणित कीटनाशक और पौष्टिक पशु आहार का विश्वसनीय स्थानीय केंद्र।"
    profile.save()
    print("✓ Business profile updated.")

    # 2. Categories
    cat_fertilizer, _ = Category.objects.get_or_create(
        slug="fertilizers",
        defaults={
            'name_hi': "उर्वरक (खाद)",
            'name_en': "Fertilizers",
            'icon': "🌾",
            'short_description': "फसल की आवश्यकतानुसार डीएपी, यूरिया, एनपीके, पोटाश, जिंक एवं माइक्रोन्यूट्रिएंट्स।",
            'badge_text': "100% असली व प्रमाणित",
            'display_order': 1
        }
    )

    cat_pesticide, _ = Category.objects.get_or_create(
        slug="pesticides",
        defaults={
            'name_hi': "कीटनाशक एवं फसल सुरक्षा",
            'name_en': "Pesticides & Crop Protection",
            'icon': "🌱",
            'short_description': "कीट, फफूंद एवं खरपतवार नियंत्रण हेतु शीर्ष कंपनियों के प्रमाणित सुरक्षा उत्पाद।",
            'badge_text': "ब्रांडेड सुरक्षा उत्पाद",
            'display_order': 2
        }
    )

    cat_cattle_feed, _ = Category.objects.get_or_create(
        slug="cattle-feed",
        defaults={
            'name_hi': "पशु आहार एवं पोषण",
            'name_en': "Cattle Feed & Nutrition",
            'icon': "🐄",
            'short_description': "दुधारू गाय-भैंस के बेहतर स्वास्थ्य, दूध व फैट वृद्धि के लिए पौष्टिक एवं संतुलित पशु आहार।",
            'badge_text': "दूध व फैट वृद्धि",
            'display_order': 3
        }
    )

    cat_seeds, _ = Category.objects.get_or_create(
        slug="seeds",
        defaults={
            'name_hi': "उन्नत हाइब्रिड बीज",
            'name_en': "Hybrid Seeds",
            'icon': "🌻",
            'short_description': "गेहूँ, धान, सरसों, मक्का, बाजरा एवं सब्जियों के उच्च अंकुरण व पैदावार वाले बीज।",
            'badge_text': "उच्च अंकुरण क्षमता",
            'display_order': 4
        }
    )
    print("✓ Categories created.")

    # 3. Products
    products_data = [
        # Fertilizers
        {
            'category': cat_fertilizer,
            'name': "इफको डीएपी (IFFCO DAP 18-46-0)",
            'slug': "iffco-dap-fertilizer",
            'brand': "IFFCO (इफको)",
            'pack_size': "50 kg बोरी",
            'short_description': "जड़ों के मजबूत विकास और पौधों की शुरुआती वृद्धि के लिए 18% नाइट्रोजन और 46% फास्फोरस युक्त उत्तम उर्वरक।",
            'detailed_description': """इफको डीएपी (डाई-अमोनियम फास्फेट) भारतीय किसानों का सबसे पसंदीदा फास्फेटिक उर्वरक है।
मुख्य विशेषताएँ:
- जड़ों का तेजी से और गहरा फैलाव।
- कल्ले फूटने में अत्यधिक सहायक।
- बुवाई के समय बेसल डोज के रूप में उपयुक्त।
उपयोग विधि: बुवाई के समय खेत में आखिरी जुताई के दौरान अथवा सीड-ड्रिल के माध्यम से बीज के साथ उचित दूरी पर डालें।""",
            'suitable_crops': "गेहूँ, धान, गन्ना, आलू, सरसों, मक्का, दलहन एवं तिलहन",
            'availability_status': 'in_stock',
            'is_featured': True,
            'price_label': "आज का सरकारी/दुकान भाव पूछें",
        },
        {
            'category': cat_fertilizer,
            'name': "नीम लेपित यूरिया (Neem Coated Urea)",
            'slug': "neem-coated-urea",
            'brand': "IFFCO / KRIBHCO",
            'pack_size': "45 kg बोरी",
            'short_description': "46% नाइट्रोजन युक्त नीम कोटेड यूरिया जो पौधों को हरा-भरा रखने और वानस्पतिक बढ़वार के लिए आवश्यक है।",
            'detailed_description': """नीम लेपित यूरिया से नाइट्रोजन धीरे-धीरे मिट्टी में घुलती है जिससे फसल को लम्बे समय तक पोषण मिलता है और बर्बादी कम होती है।
फसल के पहले और दूसरे पानी पर टॉप ड्रेसिंग के रूप में उपयोग करें।""",
            'suitable_crops': "सभी प्रमुख खाद्यान्न फसलें, गन्ना, सब्जियाँ व बागवानी",
            'availability_status': 'in_stock',
            'is_featured': True,
            'price_label': "आज का भाव पूछें",
        },
        {
            'category': cat_fertilizer,
            'name': "इफको एनपीके (IFFCO NPK 12:32:16)",
            'slug': "iffco-npk-12-32-16",
            'brand': "IFFCO (इफको)",
            'pack_size': "50 kg बोरी",
            'short_description': "नाइट्रोजन, फास्फोरस और पोटाश का संतुलित कॉम्प्लेक्स उर्वरक जो फसल को सर्वांगीण शक्ति प्रदान करता है।",
            'detailed_description': "दाने की चमक, वजन और रोग प्रतिरोधक क्षमता बढ़ाने में विशेष रूप से उपयोगी।",
            'suitable_crops': "गेहूँ, आलू, गन्ना, तिलहन एवं सब्जियाँ",
            'availability_status': 'in_stock',
            'is_featured': True,
            'price_label': "आज का भाव पूछें",
        },
        {
            'category': cat_fertilizer,
            'name': "जिंक सल्फेट 33% (Zinc Sulphate Monohydrate)",
            'slug': "zinc-sulphate-33",
            'brand': "उत्तम / दयाल / इफको",
            'pack_size': "4 kg / 5 kg बैग",
            'short_description': "फसलों में खैरा रोग और पत्तियों के पीलेपन को दूर करने हेतु उच्च गुणवत्ता वाला जिंक व सल्फर पोषण।",
            'detailed_description': "धान और गेहूँ की फसल में जिंक की कमी को पूरा करके बढ़वार तेज करता है।",
            'suitable_crops': "धान, गेहूँ, मक्का, गन्ना",
            'availability_status': 'in_stock',
            'is_featured': False,
            'price_label': "आज का भाव पूछें",
        },

        # Pesticides
        {
            'category': cat_pesticide,
            'name': "कोराजन कीटनाशक (Coragen Insecticide)",
            'slug': "fmc-coragen-insecticide",
            'brand': "FMC",
            'pack_size': "150 ml / 60 ml बोतल",
            'short_description': "गन्ने के कंसुआ (Top Borer) और तना छेदक कीटों के रोकथाम के लिए प्रसिद्ध और प्रभावी कीटनाशक।",
            'detailed_description': """कोराजन फसलों में इल्ली व तना छेदक कीटों के लंबे समय तक नियंत्रण के लिए जाना जाता है।
सुरक्षा चेतावनी: पैकेट पर दिए निर्देशानुसार पानी की सही मात्रा के साथ ड्रेंचिंग या छिड़काव करें। सुरक्षा दस्ताने और मास्क का प्रयोग करें।""",
            'suitable_crops': "गन्ना, धान, मक्का, सब्जियाँ",
            'availability_status': 'in_stock',
            'is_featured': True,
            'price_label': "आज का भाव पूछें",
        },
        {
            'category': cat_pesticide,
            'name': "कॉन्फिडोर (Confidor - Imidacloprid 17.8% SL)",
            'slug': "bayer-confidor",
            'brand': "Bayer (बायर)",
            'pack_size': "100 ml / 250 ml / 500 ml",
            'short_description': "माहू (Aphids), तेला, हरा फुदका व रस चूसक कीटों के प्रभावी नियंत्रण हेतु सिस्टेमिक कीटनाशक।",
            'detailed_description': "रस चूसक कीटों पर त्वरित असर करता है। विशेषज्ञ सलाह और लेबल निर्देशों का अनुपालन करें।",
            'suitable_crops': "सरसों, धान, कपास, सब्जियाँ, आम",
            'availability_status': 'in_stock',
            'is_featured': True,
            'price_label': "आज का भाव पूछें",
        },
        {
            'category': cat_pesticide,
            'name': "साफ फफूंदनाशक (SAAF Fungicide)",
            'slug': "upl-saaf-fungicide",
            'brand': "UPL",
            'pack_size': "250 gm / 500 gm / 1 kg",
            'short_description': "कार्बेन्डाजिम 12% + मैंकोजेब 63% WP युक्त दोहरा असरदार फफूंदनाशक, जो झुलसा व फफूंद रोगों को रोकता है।",
            'detailed_description': "बीज शोधन और पत्तियों पर छिड़काव दोनों के लिए उपयुक्त व्यापक फफूंदनाशक।",
            'suitable_crops': "आलू, धान, मूंगफली, सब्जियाँ",
            'availability_status': 'in_stock',
            'is_featured': False,
            'price_label': "आज का भाव पूछें",
        },

        # Cattle Feed
        {
            'category': cat_cattle_feed,
            'name': "गोदरेज पशु आहार - दूध धारा (Doodh Dhara)",
            'slug': "godrej-doodh-dhara-cattle-feed",
            'brand': "Godrej Agrovet",
            'pack_size': "50 kg बोरी (Pellet)",
            'short_description': "20% प्रोटीन, मिनरल्स व विटामिन युक्त संतुलित पेलेट दाना जो गाय-भैंस में दूध व फैट की मात्रा बढ़ाता है।",
            'detailed_description': """गोदरेज दूध धारा दुधारू पशुओं के पाचन और स्वास्थ्य के लिए विशेष रूप से तैयार किया गया है।
- दूध की मात्रा में स्वाभाविक वृद्धि।
- फैट और एसएनएफ (SNF) में सुधार।
- पशु के गर्भाधान चक्र को नियमित रखने में सहायक।""",
            'suitable_crops': "गाय, भैंस, दुधारू एवं गाभिन पशु",
            'availability_status': 'in_stock',
            'is_featured': True,
            'price_label': "आज का भाव पूछें",
        },
        {
            'category': cat_cattle_feed,
            'name': "कपिला पशु आहार - सुपर गोल्ड (Kapila Super Gold)",
            'slug': "kapila-super-gold-cattle-feed",
            'brand': "Kapila Pashu Aahar",
            'pack_size': "50 kg बोरी",
            'short_description': "उच्च ऊर्जा व पाचक तत्वों से भरपूर लोकप्रिय पशु आहार, दुधारू पशुओं के लिए अत्यंत लाभकारी।",
            'detailed_description': "पशुओं की सेहत बनाए रखता है और मौसम के बदलाव के समय पशुओं को तनावमुक्त रखता है।",
            'suitable_crops': "गाय, भैंस, डेयरी पशु",
            'availability_status': 'in_stock',
            'is_featured': True,
            'price_label': "आज का भाव पूछें",
        },
        {
            'category': cat_cattle_feed,
            'name': "एग्रीमिन फोर्ट मिनरल मिक्सचर (Agrimin Forte)",
            'slug': "agrimin-forte-mineral-mixture",
            'brand': "Virbac",
            'pack_size': "1 kg / 5 kg पैक",
            'short_description': "पशुओं में खनिज तत्वों (कैल्शियम, फास्फोरस, जिंक आदि) की कमी दूर करने हेतु चेलेटेड मिनरल मिक्सचर।",
            'detailed_description': "प्रतिदिन 50 ग्राम चारे में मिलाकर देने से पशु का स्वास्थ्य बेहतर रहता है और बांझपन की समस्या दूर होती है।",
            'suitable_crops': "गाय, भैंस, बछड़े",
            'availability_status': 'in_stock',
            'is_featured': False,
            'price_label': "आज का भाव पूछें",
        },

        # Seeds
        {
            'category': cat_seeds,
            'name': "पायनियर हाइब्रिड सरसों बीज 45S46 (Pioneer 45S46)",
            'slug': "pioneer-mustard-seeds-45s46",
            'brand': "Pioneer (Corteva)",
            'pack_size': "1 kg थैली",
            'short_description': "अधिक तेल प्रतिशत (41-42%) और मजबूत तने वाली उच्च पैदावार हाइब्रिड सरसों।",
            'detailed_description': "पाले और झुलसा के प्रति सहनशील, दाने चमकदार और वजनदार।",
            'suitable_crops': "सरसों रबी सीजन",
            'availability_status': 'in_stock',
            'is_featured': True,
            'price_label': "आज का भाव पूछें",
        },
        {
            'category': cat_seeds,
            'name': "उन्नत गेहूँ बीज (HD 2967 / HD 3086)",
            'slug': "wheat-seeds-hd-2967",
            'brand': "प्रमाणित राष्ट्रीय बीज निगम (NSC / UP Seeds)",
            'pack_size': "40 kg बोरी",
            'short_description': "पीला रतुआ प्रतिरोधी, चमकदार दाना और प्रति एकड़ बंपर पैदावार देने वाली लोकप्रिय गेहूँ प्रजाति।",
            'detailed_description': "समय पर बुवाई के लिए सर्वोत्तम। उच्च कल्ले फूटने की क्षमता।",
            'suitable_crops': "गेहूँ रबी सीजन",
            'availability_status': 'in_stock',
            'is_featured': False,
            'price_label': "आज का भाव पूछें",
        },
    ]

    for p in products_data:
        Product.objects.update_or_create(
            slug=p['slug'],
            defaults=p
        )
    print("✓ Products created.")

    # 4. Crop Guides (फसल मार्गदर्शिका)
    crops_data = [
        {
            'crop_name_hi': "गेहूँ (Wheat)",
            'crop_name_en': "Wheat",
            'slug': "wheat-gehun",
            'icon': "🌾",
            'season': "रबी सीजन (Rabi)",
            'sowing_time': "25 अक्टूबर से 25 नवंबर (सर्वोत्तम)",
            'summary': "गेहूँ उत्तर भारत की मुख्य खाद्यान्न फसल है। संतुलित पोषण और समय पर पहली सिंचाई (CRI स्टेज पर) करने से कल्ले अधिक फूटते हैं और उपज भरपूर मिलती है।",
            'soil_preparation': "2-3 बार गहरी जुताई कर खेत को भुरभुरा और समतल बनाएं। अंतिम जुताई के समय प्रति एकड़ 50 किलो डीएपी और 25 किलो पोटाश डालें।",
            'fertilizer_schedule': """1. बुवाई के समय: डीएपी 1 बोरी (50 किग्रा) + पोटाश (MOP) 25 किग्रा प्रति एकड़।
2. पहली सिंचाई (21 दिन पर): यूरिया 45 किग्रा + जिंक सल्फेट 33% 4 किग्रा प्रति एकड़।
3. दूसरी सिंचाई (40-45 दिन पर): यूरिया 35 किग्रा प्रति एकड़।""",
            'irrigation_info': "पहली सिंचाई 21 दिन (मुकुट जड़ अवस्था - CRI) पर अत्यंत आवश्यक है। इसके बाद कल्ले फूटते समय, गाभा अवस्था और दाना भरते समय हल्की सिंचाई करें।",
            'pest_management_tips': "चौड़ी व संकरी पत्ती वाले खरपतवारों के लिए उपयुक्त खरपतवारनाशक का प्रयोग 30-35 दिन पर करें। पीला रतुआ दिखाई देने पर विशेषज्ञ से सलाह लें।",
            'is_featured': True,
        },
        {
            'crop_name_hi': "धान (Paddy / Rice)",
            'crop_name_en': "Paddy",
            'slug': "paddy-dhaan",
            'icon': "🌱",
            'season': "खरीफ सीजन (Kharif)",
            'sowing_time': "जून - जुलाई (रोपणी)",
            'summary': "धान की रोपाई के लिए 21-25 दिन की पौध का चयन करें। लेहयुक्त खेत में जिंक और संतुलित नाइट्रोजन देने से पौधों की वृद्धि तेज होती है।",
            'soil_preparation': "खेत को अच्छी तरह पडलिंग (कदा करना) करें ताकि पानी रोकने की क्षमता बढ़ सके।",
            'fertilizer_schedule': "रोपाई के समय डीएपी 1 बोरी + पोटाश 20 किग्रा। रोपाई के 20 दिन बाद यूरिया के साथ जिंक का प्रयोग करें।",
            'irrigation_info': "रोपाई के बाद 15-20 दिनों तक खेत में 2-3 सेमी पानी बना रहे। कल्ले फूटते समय और बाली निकलते समय पानी की कमी न होने दें।",
            'pest_management_tips': "तना छेदक और पत्ती लपेटक की रोकथाम के लिए समय पर उचित कीटनाशक का छिड़काव करें।",
            'is_featured': True,
        },
        {
            'crop_name_hi': "गन्ना (Sugarcane)",
            'crop_name_en': "Sugarcane",
            'slug': "sugarcane-ganna",
            'icon': "🎋",
            'season': "शरदकालीन / वसंतकालीन",
            'sowing_time': "अक्टूबर-नवंबर अथवा फरवरी-मार्च",
            'summary': "गन्ना लंबी अवधि की नकदी फसल है। ट्रेंच विधि से बुवाई और संतुलित पोषण से प्रति एकड़ 400 से 500 क्विंटल तक पैदावार संभव है।",
            'soil_preparation': "गहरी जुताई कर ट्रेंच या कूड़ बनाएं। ट्राइकोडर्मा या फफूंदनाशक से बीज शोधन अवश्य करें।",
            'fertilizer_schedule': "बुवाई के समय डीएपी 1.5 बोरी + पोटाश 1 बोरी प्रति एकड़। पहले व दूसरे पानी पर यूरिया का प्रयोग करें।",
            'irrigation_info': "गर्मी के मौसम में 10-12 दिन के अंतराल पर सिंचाई करते रहें।",
            'pest_management_tips': "कंसुआ (Top Borer) और दीमक की रोकथाम हेतु बुवाई के समय अथवा पहली सिंचाई पर उचित कीटनाशक का प्रयोग करें।",
            'is_featured': True,
        },
        {
            'crop_name_hi': "सरसों (Mustard)",
            'crop_name_en': "Mustard",
            'slug': "mustard-sarson",
            'icon': "🌻",
            'season': "रबी सीजन (Rabi)",
            'sowing_time': "अक्टूबर का प्रथम पखवाड़ा",
            'summary': "सरसों में सल्फर का प्रयोग तेल की मात्रा और दानों की चमक बढ़ाने के लिए अनिवार्य है। समय पर बुवाई से माहू कीट का प्रकोप कम होता है।",
            'soil_preparation': "बारीक और नमीयुक्त खेत में 1.5 से 2 किलो प्रति एकड़ बीज दर रखें।",
            'fertilizer_schedule': "डीएपी 35-40 किग्रा + सल्फर 90% (बेंटोनाइट) 10 किग्रा प्रति एकड़ बुवाई के समय डालें।",
            'irrigation_info': "पहली सिंचाई बुवाई के 30-35 दिन बाद (फूल आने से ठीक पहले) और दूसरी सिंचाई फली बनते समय करें।",
            'pest_management_tips': "माहू (चेपा) दिखने पर मौसम साफ होने पर अनुशंसित कीटनाशक का छिड़काव करें।",
            'is_featured': True,
        },
        {
            'crop_name_hi': "आलू (Potato)",
            'crop_name_en': "Potato",
            'slug': "potato-aloo",
            'icon': "🥔",
            'season': "रबी सीजन",
            'sowing_time': "15 अक्टूबर से 10 नवंबर",
            'summary': "आलू की बेहतर कंद वृद्धि के लिए पोटाश और फास्फोरस की उचित मात्रा तथा अगेती-पिछेती झुलसा से बचाव जरूरी है।",
            'soil_preparation': "खेत में गोबर की सड़ी खाद मिलाकर भुरभुरा बनाएं।",
            'fertilizer_schedule': "एनपीके 12:32:16 दो बोरी + जिंक व सल्फर बुवाई के समय कूड़ों में डालें।",
            'irrigation_info': "हल्की और नियमित सिंचाई करें ताकि मेड़ें न डूबें और कंदों का विकास अच्छा हो।",
            'pest_management_tips': "झुलसा रोग से बचाव के लिए मौसम में कोहरा या बादल छाने पर फफूंदनाशक का छिड़काव करें।",
            'is_featured': True,
        },
        {
            'crop_name_hi': "मक्का (Maize)",
            'crop_name_en': "Maize",
            'slug': "maize-makka",
            'icon': "🌽",
            'season': "खरीफ / जायद / रबी",
            'sowing_time': "जून-जुलाई अथवा फरवरी-मार्च",
            'summary': "मक्का कम समय में तैयार होने वाली बहुउपयोगी फसल है। फॉल आर्मीवर्म कीट की निगरानी और समय पर नियंत्रण महत्वपूर्ण है।",
            'soil_preparation': "जल निकासी वाली दोमट मिट्टी में 2-3 जुताई कर तैयार करें।",
            'fertilizer_schedule': "डीएपी 1 बोरी + पोटाश 20 किग्रा + यूरिया को 3 भागों में बांटकर दें।",
            'irrigation_info': "नरमंजरी निकलते समय और भुट्टे में दाना भरते समय पानी की कमी न होने दें।",
            'pest_management_tips': "फॉल आर्मीवर्म के प्रकोप पर अनुमोदित कीटनाशक का शाम के समय छिड़काव करें।",
            'is_featured': True,
        },
    ]

    for c in crops_data:
        CropGuide.objects.update_or_create(
            slug=c['slug'],
            defaults=c
        )
    print("✓ Crop guides created.")

    # 5. Farmer Tips (किसान सलाह लेख)
    tips_data = [
        {
            'title': "गेहूँ की फसल में कल्ले फूटते समय खाद और पानी का सही तालमेल",
            'slug': "wheat-tillering-fertilizer-irrigation",
            'category': "soil_fertilizer",
            'summary': "बुवाई के 21 से 25 दिन बाद पहली सिंचाई और यूरिया+जिंक का संतुलित प्रयोग गेहूँ में अधिक कल्ले और बंपर पैदावार की नींव रखता है।",
            'content': """गेहूँ की बुवाई के 21 दिन बाद मुकुट जड़ (Crown Root Initiation - CRI) निकलती है। यदि इस समय पानी और पोषण की कमी हो जाए तो कल्ले कम बनते हैं।

मुख्य सुझाव:
1. सिंचाई हल्की करें, खेत में पानी भरा न रहने दें।
2. प्रति एकड़ 40-45 किलो यूरिया के साथ 4 किलो जिंक सल्फेट 33% मिलाकर ओट आने पर छिड़काव करें।
3. खरपतवार नाशक का प्रयोग पहली सिंचाई के 7-10 दिन बाद नमी में करें।""",
            'is_published': True,
            'is_featured': True,
            'published_date': datetime.date.today(),
        },
        {
            'title': "फसल में रस चूसक कीट व माहू दिखने पर क्या करें?",
            'slug': "pest-control-aphids-management",
            'category': "crop_protection",
            'summary': "मौसम में नमी और बादल होने पर फसलों में माहू और रस चूसक कीटों का खतरा बढ़ जाता है। समय पर पहचान और उचित छिड़काव से फसल सुरक्षित रखें।",
            'content': """सरसों, सब्जियों और दलहन में अक्सर माहू (Aphids) पत्तियों और फूलों का रस चूसकर पौधे को कमजोर कर देते हैं।

रोकथाम के उपाय:
1. खेत की नियमित निगरानी करें।
2. प्रारंभिक अवस्था में प्रभावित टहनियों को तोड़कर नष्ट कर दें।
3. प्रकोप बढ़ने पर बायर कॉन्फिडोर या अनुशंसित कीटनाशक का सही नाप के साथ छिड़काव करें।
4. छिड़काव हमेशा मौसम साफ होने पर और दोपहर के बाद करें।""",
            'is_published': True,
            'is_featured': True,
            'published_date': datetime.date.today() - datetime.timedelta(days=3),
        },
        {
            'title': "दुधारू पशुओं के लिए संतुलित पशु आहार का महत्व एवं सही खुराक",
            'slug': "cattle-feed-milk-yield-nutrition",
            'category': "cattle_care",
            'summary': "केवल सूखा या हरा चारा खिलाने से पशु की पोषण आवश्यकता पूरी नहीं होती। पेलेट दाना और मिनरल मिक्सचर से दूध और फैट दोनों में वृद्धि होती है।",
            'content': """दुधारू गाय-भैंस को प्रतिदिन शरीर के रख-रखाव के लिए 1.5 से 2 किलो तथा प्रति 2.5 से 3 लीटर दूध उत्पादन पर 1 किलो संतुलित पशु आहार (दाना) देना चाहिए।

फायदे:
- दूध उत्पादन में 15-20% की बढ़ोतरी।
- दूध में फैट और एसएनएफ (SNF) का स्तर सुधरता है।
- पशु समय पर गर्मी (हीट) में आता है और बार-बार नहीं पलटता।
- प्रतिदिन 40-50 ग्राम मिनरल मिक्सचर चारे में जरूर मिलाएं।""",
            'is_published': True,
            'is_featured': True,
            'published_date': datetime.date.today() - datetime.timedelta(days=7),
        },
    ]

    for t in tips_data:
        FarmerTip.objects.update_or_create(
            slug=t['slug'],
            defaults=t
        )
    print("✓ Farmer tips created.")

    # 6. Offers
    offers_data = [
        {
            'title': "मौसमी बुवाई विशेष बचत: जिंक + सल्फर कॉम्बो ऑफर",
            'badge_text': "सीमित समय ऑफर",
            'description': "गेहूँ एवं सरसों बुवाई के अवसर पर जिंक सल्फेट और बेंटोनाइट सल्फर के कॉम्बो पैक पर विशेष छूट। दुकान पर उपलब्धता की जाँच तुरंत करें।",
            'deal_highlight': "कॉम्बो पैक पर आकर्षक बचत",
            'valid_from': datetime.date.today(),
            'valid_until': datetime.date.today() + datetime.timedelta(days=30),
            'is_active': True,
            'display_order': 1,
        },
        {
            'title': "पशु आहार 5 बोरी खरीद पर विशेष छूट व उपहार",
            'badge_text': "डेयरी किसान विशेष",
            'description': "गोदरेज दूध धारा या कपिला सुपर गोल्ड की 5 या अधिक बोरियों की एकमुश्त खरीद पर विशेष थोक दर व उपहार।",
            'deal_highlight': "थोक भाव व आसान डिलीवरी परामर्श",
            'valid_from': datetime.date.today(),
            'valid_until': datetime.date.today() + datetime.timedelta(days=45),
            'is_active': True,
            'display_order': 2,
        },
    ]

    for o in offers_data:
        Offer.objects.get_or_create(
            title=o['title'],
            defaults=o
        )
    print("✓ Offers created.")

    # 7. Real Reviews (Approved)
    reviews_data = [
        {
            'customer_name': "रामेश्वर सिंह",
            'village_location': "गाँव: रायपुर, सीतापुर",
            'rating': 5,
            'review_text': "रस्तोगी ट्रेडर्स से पिछले 4 सालों से खाद और दवा ले रहा हूँ। यहाँ कभी नकली सामान नहीं मिला और हर खाद का भाव भी एकदम सही रहता है।",
            'is_approved': True,
            'display_order': 1,
        },
        {
            'customer_name': "वीरेंद्र यादव (डेयरी संचालक)",
            'village_location': "गाँव: पिपरिया, लखीमपुर रोड",
            'rating': 5,
            'review_text': "इनकी दुकान का गोदरेज पशु आहार खिलाने से मेरी 8 भैंसों का दूध और फैट दोनों बढ़ गया। समय पर माल मिल जाता है।",
            'is_approved': True,
            'display_order': 2,
        },
        {
            'customer_name': "मोहित वर्मा (किसान)",
            'village_location': "गाँव: हरगांव परिक्षेत्र",
            'rating': 5,
            'review_text': "WhatsApp पर आज का भाव पूछने पर तुरंत जवाब आ जाता है। दुकान पर जाने से पहले ही पता चल जाता है कि स्टॉक उपलब्ध है या नहीं। बहुत बढ़िया सुविधा।",
            'is_approved': True,
            'display_order': 3,
        },
    ]

    for r in reviews_data:
        Review.objects.get_or_create(
            customer_name=r['customer_name'],
            village_location=r['village_location'],
            defaults=r
        )
    print("✓ Customer reviews created.")

    # 8. Gallery Images placeholder
    gallery_data = [
        {'title': "उर्वरक एवं खाद स्टॉक काउंटर", 'category': 'shop', 'caption': "इफको डीएपी एवं यूरिया का ताजा स्टॉक", 'is_featured': True, 'display_order': 1},
        {'title': "पशु आहार भंडार कक्ष", 'category': 'cattle_feed', 'caption': "गोदरेज एवं कपिला पशु आहार बोरियां", 'is_featured': True, 'display_order': 2},
        {'title': "प्रमाणित बीज एवं कीटनाशक शेल्फ", 'category': 'stock', 'caption': "सीलबंद और ऑरिजिनल फसल सुरक्षा उत्पाद", 'is_featured': True, 'display_order': 3},
        {'title': "लहलहाती गेहूँ की फसल", 'category': 'farmers', 'caption': "हमारे नियमित किसान भाई के खेत का दृश्य", 'is_featured': True, 'display_order': 4},
        {'title': "दुकान का मुख्य प्रवेश द्वार", 'category': 'shop', 'caption': "मंडी रोड पर मुख्य प्रवेश व पार्किंग सुविधा", 'is_featured': True, 'display_order': 5},
        {'title': "दुधारू पशु व डेयरी पोषण", 'category': 'cattle_feed', 'caption': "संतुलित आहार से स्वस्थ पशु", 'is_featured': True, 'display_order': 6},
    ]

    for g in gallery_data:
        GalleryImage.objects.get_or_create(
            title=g['title'],
            defaults=g
        )
    print("✓ Gallery items created.")

    print("🎉 All seed data populated successfully!")


if __name__ == "__main__":
    seed_database()
