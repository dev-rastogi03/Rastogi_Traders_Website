import re
from django import forms
from django.core.exceptions import ValidationError
from .models import ContactMessage, Review


class ContactForm(forms.ModelForm):
    # Hidden Honeypot Field for anti-bot spam protection
    website_url = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'style': 'display:none !important; visibility:hidden !important; position:absolute !important; left:-9999px !important;',
            'tabindex': '-1',
            'autocomplete': 'off',
            'aria-hidden': 'true',
        })
    )

    CATEGORY_CHOICES = [
        ('', '-- आवश्यक उत्पाद / विषय चुनें --'),
        ('उर्वरक (Fertilizers)', 'उर्वरक (Fertilizers - DAP, Urea, NPK आदि)'),
        ('कीटनाशक (Pesticides)', 'कीटनाशक एवं फसल सुरक्षा (Pesticides / Fungicides)'),
        ('पशु आहार (Cattle Feed)', 'पशु आहार एवं डेयरी पोषण (Cattle Feed)'),
        ('उन्नत बीज (Seeds)', 'उन्नत बीज (Hybrid Seeds)'),
        ('सामान्य पूछताछ (General)', 'अन्य / सामान्य जानकारी'),
    ]

    interested_category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'contact-category-input'
        })
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'village', 'interested_category', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'उदा. रमेश कुमार / अपना शुभ नाम',
                'required': True,
                'maxlength': '100',
                'id': 'contact-name-input'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'उदा. 9876543210 (10 अंकों का नंबर)',
                'required': True,
                'type': 'tel',
                'maxlength': '15',
                'id': 'contact-phone-input'
            }),
            'village': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'उदा. गाँव - रामपुर, पोस्ट - हरगांव',
                'maxlength': '120',
                'id': 'contact-village-input'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'आप किस खाद, बीज या कीटनाशक की उपलब्धता व भाव जानना चाहते हैं? यहाँ लिखें...',
                'required': True,
                'maxlength': '1000',
                'id': 'contact-message-input'
            }),
        }

    def clean_website_url(self):
        # Honeypot validation: if filled by a bot, reject
        value = self.cleaned_data.get('website_url')
        if value:
            raise ValidationError("Spam bot submission detected.")
        return value

    def clean_phone(self):
        raw_phone = self.cleaned_data.get('phone', '').strip()
        # Remove spaces, dashes, +91, leading 0
        cleaned = re.sub(r'[\s\-\(\)\+]', '', raw_phone)
        if cleaned.startswith('91') and len(cleaned) == 12:
            cleaned = cleaned[2:]
        elif cleaned.startswith('0') and len(cleaned) == 11:
            cleaned = cleaned[1:]

        # Validate standard Indian 10-digit mobile number format
        if not re.match(r'^[6-9]\d{9}$', cleaned):
            raise ValidationError("कृपया सही 10 अंकों का भारतीय मोबाइल नंबर दर्ज करें (उदा. 9876543210)।")
        
        return cleaned

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 2:
            raise ValidationError("कृपया अपना पूरा नाम दर्ज करें (कम से कम 2 अक्षर)।")
        return name

    def clean_message(self):
        message = self.cleaned_data.get('message', '').strip()
        if len(message) < 5:
            raise ValidationError("कृपया अपना संदेश या सवाल विस्तार से लिखें (कम से कम 5 अक्षर)।")
        return message


class ReviewSubmissionForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['customer_name', 'village_location', 'rating', 'review_text']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'आपका नाम',
                'required': True
            }),
            'village_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'गाँव / कस्बा',
                'required': True
            }),
            'rating': forms.Select(attrs={
                'class': 'form-select'
            }),
            'review_text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'रस्तोगी ट्रेडर्स के उत्पाद और सेवा के बारे में अपना अनुभव साझा करें...',
                'required': True
            }),
        }
