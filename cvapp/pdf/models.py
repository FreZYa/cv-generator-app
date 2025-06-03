from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.urls import reverse
import uuid

# Create your models here.
class Profile(models.Model):
    # Unique identifier
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Personal Information
    name = models.CharField(
        max_length=100, 
        verbose_name="Ad Soyad",
        help_text="Tam adınızı giriniz"
    )
    email = models.EmailField(
        max_length=100, 
        validators=[EmailValidator()],
        verbose_name="E-posta Adresi",
        help_text="Geçerli bir e-posta adresi giriniz"
    )
    
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', 
        message="Telefon numarası '+999999999' formatında olmalıdır. 15 haneden fazla olamaz."
    )
    phone = models.CharField(
        validators=[phone_regex], 
        max_length=17, 
        verbose_name="Telefon Numarası",
        help_text="Örnek: +905551234567"
    )
    
    address = models.TextField(
        max_length=300, 
        blank=True, 
        null=True,
        verbose_name="Adres",
        help_text="İkamet adresiniz (Opsiyonel)"
    )
    
    # Professional Summary
    summary = models.TextField(
        max_length=2000, 
        verbose_name="Profesyonel Özet",
        help_text="Kendinizi ve kariyerinizi kısaca tanıtın"
    )
    
    # Education
    degree = models.CharField(
        max_length=100, 
        verbose_name="Eğitim Seviyesi",
        help_text="Örnek: Lisans, Yüksek Lisans, Doktora"
    )
    school = models.CharField(
        max_length=100, 
        verbose_name="Lise",
        help_text="Mezun olduğunuz lise"
    )
    university = models.CharField(
        max_length=100, 
        verbose_name="Üniversite",
        help_text="Mezun olduğunuz üniversite ve bölüm"
    )
    graduation_year = models.IntegerField(
        blank=True, 
        null=True,
        verbose_name="Mezuniyet Yılı",
        help_text="Üniversiteden mezun olduğunuz yıl"
    )
    gpa = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        blank=True, 
        null=True,
        verbose_name="GPA/Not Ortalaması",
        help_text="4.0 üzerinden not ortalamanız (Opsiyonel)"
    )
    
    # Work Experience
    previous_work = models.TextField(
        max_length=2000, 
        verbose_name="İş Deneyimi",
        help_text="Önceki iş deneyimlerinizi kronolojik sırayla yazın"
    )
    current_position = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        verbose_name="Mevcut Pozisyon",
        help_text="Şu anki çalıştığınız pozisyon (Opsiyonel)"
    )
    experience_years = models.IntegerField(
        blank=True, 
        null=True,
        verbose_name="Toplam Deneyim (Yıl)",
        help_text="Toplam çalışma deneyiminiz yıl olarak"
    )
    
    # Skills
    skills = models.TextField(
        max_length=2000, 
        verbose_name="Beceriler",
        help_text="Teknik ve kişisel becerilerinizi listeleyin"
    )
    languages = models.TextField(
        max_length=500, 
        blank=True, 
        null=True,
        verbose_name="Dil Becerileri",
        help_text="Bildiğiniz dilleri ve seviyelerini yazın (Opsiyonel)"
    )
    
    # Additional Information
    certifications = models.TextField(
        max_length=1000, 
        blank=True, 
        null=True,
        verbose_name="Sertifikalar",
        help_text="Sahip olduğunuz profesyonel sertifikalar (Opsiyonel)"
    )
    projects = models.TextField(
        max_length=1500, 
        blank=True, 
        null=True,
        verbose_name="Projeler",
        help_text="Katıldığınız önemli projeler (Opsiyonel)"
    )
    hobbies = models.TextField(
        max_length=500, 
        blank=True, 
        null=True,
        verbose_name="Hobiler",
        help_text="İlgi alanlarınız ve hobileriniz (Opsiyonel)"
    )
    
    # Social Media & Links
    linkedin_url = models.URLField(
        blank=True, 
        null=True,
        verbose_name="LinkedIn Profili",
        help_text="LinkedIn profil linkiniz (Opsiyonel)"
    )
    github_url = models.URLField(
        blank=True, 
        null=True,
        verbose_name="GitHub Profili",
        help_text="GitHub profil linkiniz (Opsiyonel)"
    )
    portfolio_url = models.URLField(
        blank=True, 
        null=True,
        verbose_name="Portfolio Website",
        help_text="Kişisel website/portfolio linkiniz (Opsiyonel)"
    )
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Son Güncelleme")
    is_active = models.BooleanField(
        default=True, 
        verbose_name="Aktif",
        help_text="CV'nin aktif olup olmadığı"
    )
    
    class Meta:
        verbose_name = "CV Profili"
        verbose_name_plural = "CV Profilleri"
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.name} - {self.email}"
    
    def get_absolute_url(self):
        return reverse('resume', kwargs={'id': self.id})
    
    def get_full_name(self):
        """Return the full name"""
        return self.name
    
    def get_short_summary(self):
        """Return a shortened version of summary for list views"""
        if len(self.summary) > 100:
            return self.summary[:100] + "..."
        return self.summary
    
    def has_social_links(self):
        """Check if profile has any social media links"""
        return any([self.linkedin_url, self.github_url, self.portfolio_url])
    
    def get_skills_list(self):
        """Return skills as a list"""
        return [skill.strip() for skill in self.skills.split(',') if skill.strip()]
    
    def get_experience_level(self):
        """Return experience level based on years"""
        if not self.experience_years:
            return "Belirtilmemiş"
        elif self.experience_years < 2:
            return "Giriş Seviyesi"
        elif self.experience_years < 5:
            return "Orta Seviye"
        elif self.experience_years < 10:
            return "Üst Seviye"
        else:
            return "Uzman Seviye"

