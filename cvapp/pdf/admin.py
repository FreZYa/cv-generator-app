from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'email', 
        'phone',
        'get_experience_level', 
        'created_at', 
        'is_active',
        'view_pdf_link',
        'view_profile_link'
    ]
    
    list_filter = [
        'is_active',
        'created_at', 
        'updated_at',
        'experience_years',
        'degree'
    ]
    
    search_fields = [
        'name', 
        'email', 
        'phone',
        'university',
        'current_position',
        'skills'
    ]
    
    readonly_fields = [
        'id',
        'created_at', 
        'updated_at',
        'get_experience_level',
        'get_skills_list',
        'has_social_links'
    ]
    
    fieldsets = (
        ('Kişisel Bilgiler', {
            'fields': (
                'id',
                'name', 
                'email', 
                'phone', 
                'address'
            )
        }),
        ('Profesyonel Özet', {
            'fields': ('summary',)
        }),
        ('Eğitim Bilgileri', {
            'fields': (
                'degree', 
                'school', 
                'university', 
                'graduation_year', 
                'gpa'
            )
        }),
        ('İş Deneyimi', {
            'fields': (
                'previous_work', 
                'current_position', 
                'experience_years',
                'get_experience_level'
            )
        }),
        ('Beceriler ve Yetenekler', {
            'fields': (
                'skills',
                'get_skills_list',
                'languages'
            )
        }),
        ('Ek Bilgiler', {
            'fields': (
                'certifications', 
                'projects', 
                'hobbies'
            ),
            'classes': ('collapse',)
        }),
        ('Sosyal Medya ve Linkler', {
            'fields': (
                'linkedin_url', 
                'github_url', 
                'portfolio_url',
                'has_social_links'
            ),
            'classes': ('collapse',)
        }),
        ('Meta Bilgiler', {
            'fields': (
                'created_at', 
                'updated_at', 
                'is_active'
            ),
            'classes': ('collapse',)
        }),
    )
    
    list_per_page = 20
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    actions = ['make_active', 'make_inactive', 'export_as_csv']
    
    def view_pdf_link(self, obj):
        """Generate a link to view the PDF"""
        if obj.id:
            url = reverse('resume', kwargs={'id': obj.id})
            return format_html(
                '<a href="{}" target="_blank" class="button">📄 PDF Görüntüle</a>',
                url
            )
        return '-'
    view_pdf_link.short_description = 'PDF'
    
    def view_profile_link(self, obj):
        """Generate a link to view the profile"""
        if obj.id:
            url = reverse('profile_preview', kwargs={'id': obj.id})
            return format_html(
                '<a href="{}" target="_blank" class="button">👁️ Önizleme</a>',
                url
            )
        return '-'
    view_profile_link.short_description = 'Önizleme'
    
    def get_skills_list(self, obj):
        """Display skills as a formatted list"""
        skills = obj.get_skills_list()
        if skills:
            skills_html = '<br>'.join([f'• {skill}' for skill in skills[:5]])
            if len(skills) > 5:
                skills_html += f'<br><em>... ve {len(skills)-5} beceri daha</em>'
            return mark_safe(skills_html)
        return '-'
    get_skills_list.short_description = 'Beceriler'
    
    def has_social_links(self, obj):
        """Show if profile has social media links"""
        if obj.has_social_links():
            links = []
            if obj.linkedin_url:
                links.append('LinkedIn')
            if obj.github_url:
                links.append('GitHub')
            if obj.portfolio_url:
                links.append('Portfolio')
            return ', '.join(links)
        return 'Yok'
    has_social_links.short_description = 'Sosyal Medya'
    
    def make_active(self, request, queryset):
        """Mark selected profiles as active"""
        updated = queryset.update(is_active=True)
        self.message_user(
            request, 
            f'{updated} CV profili aktif olarak işaretlendi.'
        )
    make_active.short_description = 'Seçili CV\'leri aktif yap'
    
    def make_inactive(self, request, queryset):
        """Mark selected profiles as inactive"""
        updated = queryset.update(is_active=False)
        self.message_user(
            request, 
            f'{updated} CV profili inaktif olarak işaretlendi.'
        )
    make_inactive.short_description = 'Seçili CV\'leri inaktif yap'
    
    def export_as_csv(self, request, queryset):
        """Export selected profiles as CSV"""
        import csv
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="cv_profiles.csv"'
        response.write('\ufeff'.encode('utf8'))  # BOM for Excel compatibility
        
        writer = csv.writer(response)
        writer.writerow([
            'Ad Soyad', 'E-posta', 'Telefon', 'Derece', 'Üniversite',
            'Deneyim Yılı', 'Oluşturulma Tarihi', 'Aktif'
        ])
        
        for profile in queryset:
            writer.writerow([
                profile.name,
                profile.email,
                profile.phone,
                profile.degree,
                profile.university,
                profile.experience_years or 0,
                profile.created_at.strftime('%Y-%m-%d %H:%M'),
                'Evet' if profile.is_active else 'Hayır'
            ])
        
        return response
    export_as_csv.short_description = 'Seçili CV\'leri CSV olarak dışa aktar'
    
    def get_queryset(self, request):
        """Optimize queryset for admin"""
        return super().get_queryset(request).select_related()
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }
        js = ('admin/js/custom_admin.js',)
