from django import forms
from .models import ContactMessage, Review


class ContactForm(forms.ModelForm):
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
                'id': 'contact-name-input'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'उदा. 9876543210 (10 अंकों का नंबर)',
                'required': True,
                'type': 'tel',
                'id': 'contact-phone-input'
            }),
            'village': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'उदा. गाँव - रामपुर, पोस्ट - हरगांव',
                'id': 'contact-village-input'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'आप किस खाद, बीज या कीटनाशक की उपलब्धता व भाव जानना चाहते हैं? यहाँ लिखें...',
                'required': True,
                'id': 'contact-message-input'
            }),
        }


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
