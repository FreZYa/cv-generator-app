from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'created_at', 'updated_at', 'is_active']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Adınız ve soyadınızı giriniz',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ornek@email.com',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+90 555 123 4567',
                'required': True
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tam adresinizi giriniz',
                'rows': 3,
                'maxlength': 300
            }),
            'summary': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Kendinizi ve kariyerinizi kısaca tanıtın...',
                'rows': 5,
                'maxlength': 2000,
                'required': True
            }),
            'degree': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Lisans, Yüksek Lisans, Doktora...',
                'required': True
            }),
            'school': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mezun olduğunuz lise',
                'required': True
            }),
            'university': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Üniversite ve bölüm adı',
                'required': True
            }),
            'graduation_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '2023',
                'min': 1950,
                'max': 2030
            }),
            'gpa': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '3.50',
                'step': 0.01,
                'min': 0,
                'max': 4
            }),
            'previous_work': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'İş deneyimlerinizi kronolojik sırayla yazın...',
                'rows': 6,
                'maxlength': 2000,
                'required': True
            }),
            'current_position': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mevcut pozisyonunuz'
            }),
            'experience_years': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '5',
                'min': 0,
                'max': 50
            }),
            'skills': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Python, JavaScript, Django, React... (virgülle ayırın)',
                'rows': 4,
                'maxlength': 2000,
                'required': True
            }),
            'languages': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Türkçe (Ana dili), İngilizce (İleri), Almanca (Orta)...',
                'rows': 3,
                'maxlength': 500
            }),
            'certifications': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'AWS Certified, Google Analytics, Microsoft Office...',
                'rows': 4,
                'maxlength': 1000
            }),
            'projects': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Katıldığınız önemli projeleri açıklayın...',
                'rows': 5,
                'maxlength': 1500
            }),
            'hobbies': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Kitap okuma, spor, müzik, seyahat...',
                'rows': 3,
                'maxlength': 500
            }),
            'linkedin_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://linkedin.com/in/kullanici-adi'
            }),
            'github_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://github.com/kullanici-adi'
            }),
            'portfolio_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://website.com'
            }),
        }
        
        labels = {
            'name': 'Ad Soyad *',
            'email': 'E-posta Adresi *',
            'phone': 'Telefon Numarası *',
            'address': 'Adres',
            'summary': 'Profesyonel Özet *',
            'degree': 'Eğitim Seviyesi *',
            'school': 'Lise *',
            'university': 'Üniversite ve Bölüm *',
            'graduation_year': 'Mezuniyet Yılı',
            'gpa': 'GPA/Not Ortalaması',
            'previous_work': 'İş Deneyimi *',
            'current_position': 'Mevcut Pozisyon',
            'experience_years': 'Toplam Deneyim (Yıl)',
            'skills': 'Beceriler *',
            'languages': 'Dil Becerileri',
            'certifications': 'Sertifikalar',
            'projects': 'Projeler',
            'hobbies': 'Hobiler ve İlgi Alanları',
            'linkedin_url': 'LinkedIn Profili',
            'github_url': 'GitHub Profili',
            'portfolio_url': 'Portfolio/Website',
        }
        
        help_texts = {
            'name': 'Tam adınızı ve soyadınızı giriniz',
            'email': 'Geçerli bir e-posta adresi giriniz',
            'phone': 'Örnek: +90 555 123 4567',
            'address': 'İkamet adresiniz (opsiyonel)',
            'summary': 'Kendinizi ve kariyerinizi kısaca tanıtın (maksimum 2000 karakter)',
            'degree': 'Eğitim seviyenizi belirtiniz',
            'school': 'Mezun olduğunuz liseyi yazınız',
            'university': 'Üniversite ve bölüm adını yazınız',
            'graduation_year': 'Mezun olduğunuz yılı giriniz',
            'gpa': '4.0 üzerinden not ortalamanız (opsiyonel)',
            'previous_work': 'İş deneyimlerinizi kronolojik sırayla yazın',
            'current_position': 'Şu anki pozisyonunuz (opsiyonel)',
            'experience_years': 'Toplam çalışma deneyiminiz',
            'skills': 'Teknik ve kişisel becerilerinizi virgülle ayırarak yazın',
            'languages': 'Bildiğiniz dilleri ve seviyelerini yazın',
            'certifications': 'Sahip olduğunuz profesyonel sertifikaları yazın',
            'projects': 'Katıldığınız önemli projeleri açıklayın',
            'hobbies': 'İlgi alanlarınızı ve hobilerinizi yazın',
            'linkedin_url': 'LinkedIn profil linkinizi giriniz',
            'github_url': 'GitHub profil linkinizi giriniz',
            'portfolio_url': 'Kişisel website veya portfolio linkinizi giriniz',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add form-label class to all labels
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] += ' fade-in'
            
        # Set required fields
        required_fields = ['name', 'email', 'phone', 'summary', 'degree', 'school', 'university', 'previous_work', 'skills']
        for field_name in required_fields:
            self.fields[field_name].required = True
            
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            # Remove any non-digit characters except +
            import re
            phone = re.sub(r'[^\d+]', '', phone)
        return phone
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            email = email.lower().strip()
        return email
    
    def clean_graduation_year(self):
        graduation_year = self.cleaned_data.get('graduation_year')
        if graduation_year:
            import datetime
            current_year = datetime.datetime.now().year
            if graduation_year > current_year + 10:
                raise forms.ValidationError('Mezuniyet yılı çok gelecekte olamaz.')
            if graduation_year < 1950:
                raise forms.ValidationError('Mezuniyet yılı çok geçmişte olamaz.')
        return graduation_year
    
    def clean_gpa(self):
        gpa = self.cleaned_data.get('gpa')
        if gpa and (gpa < 0 or gpa > 4):
            raise forms.ValidationError('GPA 0.00 ile 4.00 arasında olmalıdır.')
        return gpa
    
    def clean_experience_years(self):
        experience_years = self.cleaned_data.get('experience_years')
        if experience_years and experience_years < 0:
            raise forms.ValidationError('Deneyim yılı negatif olamaz.')
        if experience_years and experience_years > 50:
            raise forms.ValidationError('Deneyim yılı 50\'den fazla olamaz.')
        return experience_years 