from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
import pdfkit
import logging

from .models import Profile
from .forms import ProfileForm

# Set up logging
logger = logging.getLogger(__name__)

def accept(request):
    """Handle CV form submission with enhanced error handling"""
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        
        if form.is_valid():
            try:
                profile = form.save()
                messages.success(
                    request, 
                    f'CV başarıyla oluşturuldu! <a href="/resume/{profile.id}" target="_blank" class="alert-link">PDF olarak görüntüle</a>',
                    extra_tags='safe'
                )
                
                # Return JSON response for AJAX requests
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'success': True,
                        'message': 'CV başarıyla oluşturuldu!',
                        'profile_id': str(profile.id),
                        'redirect_url': f'/resume/{profile.id}'
                    })
                
                return redirect('profile_list')
                
            except Exception as e:
                logger.error(f"Error saving profile: {str(e)}")
                messages.error(request, 'CV kaydedilirken bir hata oluştu. Lütfen tekrar deneyin.')
                
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'success': False,
                        'message': 'CV kaydedilirken bir hata oluştu.'
                    })
        else:
            # Form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'errors': form.errors,
                    'message': 'Form verilerinde hatalar var.'
                })
    else:
        form = ProfileForm()
    
    context = {
        'form': form,
        'title': 'CV Oluştur'
    }
    return render(request, 'accept.html', context)

def resume(request, id):
    """Generate and serve PDF resume"""
    try:
        profile = get_object_or_404(Profile, id=id, is_active=True)
        
        # Load template and render with profile data
        template = loader.get_template('resume.html')
        context = {
            'profile': profile,
            'skills_list': profile.get_skills_list(),
            'experience_level': profile.get_experience_level(),
        }
        html = template.render(context)
        
        # PDF generation options
        options = {
            'page-size': 'A4',
            'encoding': "UTF-8",
            'margin-top': '0.75in',
            'margin-right': '0.75in',   
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'print-media-type': '',
            'no-outline': None,
            'enable-local-file-access': None,
        }
        
        try:
            pdf = pdfkit.from_string(html, False, options=options)
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{profile.name}_CV.pdf"'
            
            logger.info(f"PDF generated successfully for profile {profile.id}")
            return response
            
        except Exception as pdf_error:
            logger.error(f"PDF generation error: {str(pdf_error)}")
            messages.error(request, 'PDF oluşturulurken bir hata oluştu. Lütfen tekrar deneyin.')
            return redirect('profile_list')
            
    except Profile.DoesNotExist:
        messages.error(request, 'İstenen CV bulunamadı.')
        return redirect('profile_list')
    except Exception as e:
        logger.error(f"Error in resume view: {str(e)}")
        messages.error(request, 'Bir hata oluştu. Lütfen tekrar deneyin.')
        return redirect('profile_list')

def profile_list(request):
    """Display paginated list of profiles with search functionality"""
    profiles_list = Profile.objects.filter(is_active=True).order_by('-created_at')
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        profiles_list = profiles_list.filter(
            name__icontains=search_query
        ).distinct()
    
    # Pagination
    paginator = Paginator(profiles_list, 9)  # Show 9 profiles per page
    page_number = request.GET.get('page')
    profiles = paginator.get_page(page_number)
    
    context = {
        'profiles': profiles,
        'search_query': search_query,
        'title': 'CV Listesi',
        'total_profiles': Profile.objects.filter(is_active=True).count()
    }
    return render(request, 'list.html', context)

@require_http_methods(["GET"])
def profile_preview(request, id):
    """Show profile preview without generating PDF"""
    try:
        profile = get_object_or_404(Profile, id=id, is_active=True)
        context = {
            'profile': profile,
            'skills_list': profile.get_skills_list(),
            'experience_level': profile.get_experience_level(),
            'preview_mode': True
        }
        return render(request, 'profile_preview.html', context)
    except Profile.DoesNotExist:
        messages.error(request, 'İstenen CV bulunamadı.')
        return redirect('profile_list')

def home(request):
    """Home page redirect"""
    return redirect('accept')

# Alternative view name for backward compatibility
def list(request):
    """Backward compatibility for list view"""
    return profile_list(request)
    