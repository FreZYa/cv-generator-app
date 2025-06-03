// ===== DOM Content Loaded =====
document.addEventListener('DOMContentLoaded', function() {
    
    // ===== Initialize Animations =====
    initializeAnimations();
    
    // ===== Form Enhancements =====
    enhanceForms();
    
    // ===== Button Interactions =====
    enhanceButtons();
    
    // ===== Smooth Scrolling =====
    enableSmoothScrolling();
    
    // ===== Auto-resize Textareas =====
    autoResizeTextareas();
});

// ===== Animation Functions =====
function initializeAnimations() {
    // Add fade-in class to elements
    const elements = document.querySelectorAll('.card, .form-container, .header');
    elements.forEach((element, index) => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            element.style.transition = 'all 0.6s ease';
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }, index * 100);
    });
}

// ===== Form Enhancement Functions =====
function enhanceForms() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        // Add form validation
        addFormValidation(form);
        
        // Add loading state on submit
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                addLoadingState(submitBtn);
            }
        });
        
        // Add input enhancements
        enhanceInputs(form);
    });
}

function addFormValidation(form) {
    const inputs = form.querySelectorAll('input[required], textarea[required]');
    
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateInput(this);
        });
        
        input.addEventListener('input', function() {
            clearValidationError(this);
        });
    });
}

function validateInput(input) {
    const value = input.value.trim();
    const isValid = input.checkValidity();
    
    if (!isValid || value === '') {
        showInputError(input, getErrorMessage(input));
        return false;
    } else {
        showInputSuccess(input);
        return true;
    }
}

function showInputError(input, message) {
    clearValidationState(input);
    
    input.classList.add('is-invalid');
    input.style.borderColor = '#f56565';
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.style.color = '#f56565';
    errorDiv.style.fontSize = '0.875rem';
    errorDiv.style.marginTop = '0.25rem';
    errorDiv.textContent = message;
    
    input.parentNode.appendChild(errorDiv);
}

function showInputSuccess(input) {
    clearValidationState(input);
    
    input.classList.add('is-valid');
    input.style.borderColor = '#48bb78';
}

function clearValidationError(input) {
    if (input.classList.contains('is-invalid')) {
        clearValidationState(input);
    }
}

function clearValidationState(input) {
    input.classList.remove('is-invalid', 'is-valid');
    input.style.borderColor = '';
    
    const errorMessage = input.parentNode.querySelector('.error-message');
    if (errorMessage) {
        errorMessage.remove();
    }
}

function getErrorMessage(input) {
    const type = input.type;
    const name = input.name;
    
    if (input.hasAttribute('required') && input.value.trim() === '') {
        return `${getFieldLabel(name)} alanı zorunludur.`;
    }
    
    if (type === 'email' && !input.checkValidity()) {
        return 'Geçerli bir e-posta adresi giriniz.';
    }
    
    if (type === 'tel' && !input.checkValidity()) {
        return 'Geçerli bir telefon numarası giriniz.';
    }
    
    return 'Bu alan geçerli değil.';
}

function getFieldLabel(name) {
    const labels = {
        'name': 'Ad Soyad',
        'email': 'E-posta',
        'phone': 'Telefon',
        'summary': 'Özet',
        'degree': 'Derece',
        'school': 'Okul',
        'university': 'Üniversite',
        'previous_work': 'Önceki İş Deneyimi',
        'skills': 'Beceriler'
    };
    
    return labels[name] || name;
}

function enhanceInputs(form) {
    const inputs = form.querySelectorAll('input, textarea');
    
    inputs.forEach(input => {
        // Add floating label effect
        addFloatingLabel(input);
        
        // Add character counter for textareas
        if (input.tagName === 'TEXTAREA') {
            addCharacterCounter(input);
        }
        
        // Add input formatting
        addInputFormatting(input);
    });
}

function addFloatingLabel(input) {
    const label = input.previousElementSibling;
    if (!label || label.tagName !== 'LABEL') return;
    
    function updateLabel() {
        if (input.value.trim() !== '' || input === document.activeElement) {
            label.style.transform = 'translateY(-1.5rem) scale(0.85)';
            label.style.color = '#667eea';
        } else {
            label.style.transform = 'translateY(0) scale(1)';
            label.style.color = '#718096';
        }
    }
    
    input.addEventListener('focus', updateLabel);
    input.addEventListener('blur', updateLabel);
    input.addEventListener('input', updateLabel);
    
    // Initial state
    updateLabel();
}

function addCharacterCounter(textarea) {
    const maxLength = textarea.getAttribute('maxlength');
    if (!maxLength) return;
    
    const counter = document.createElement('div');
    counter.className = 'character-counter';
    counter.style.textAlign = 'right';
    counter.style.fontSize = '0.75rem';
    counter.style.color = '#718096';
    counter.style.marginTop = '0.25rem';
    
    function updateCounter() {
        const current = textarea.value.length;
        const max = parseInt(maxLength);
        counter.textContent = `${current}/${max}`;
        
        if (current > max * 0.9) {
            counter.style.color = '#f56565';
        } else if (current > max * 0.7) {
            counter.style.color = '#ed8936';
        } else {
            counter.style.color = '#718096';
        }
    }
    
    textarea.addEventListener('input', updateCounter);
    textarea.parentNode.appendChild(counter);
    updateCounter();
}

function addInputFormatting(input) {
    if (input.type === 'tel') {
        input.addEventListener('input', function() {
            let value = this.value.replace(/\D/g, '');
            if (value.length >= 10) {
                value = value.replace(/(\d{3})(\d{3})(\d{4})/, '($1) $2-$3');
            }
            this.value = value;
        });
    }
}

// ===== Button Enhancement Functions =====
function enhanceButtons() {
    const buttons = document.querySelectorAll('.btn');
    
    buttons.forEach(button => {
        // Add ripple effect
        addRippleEffect(button);
        
        // Add accessibility
        addButtonAccessibility(button);
    });
}

function addRippleEffect(button) {
    button.addEventListener('click', function(e) {
        const ripple = document.createElement('span');
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;
        
        ripple.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            left: ${x}px;
            top: ${y}px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            transform: scale(0);
            animation: ripple 0.6s linear;
            pointer-events: none;
        `;
        
        this.style.position = 'relative';
        this.style.overflow = 'hidden';
        this.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    });
}

function addButtonAccessibility(button) {
    button.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            this.click();
        }
    });
}

function addLoadingState(button) {
    const originalText = button.textContent;
    button.disabled = true;
    button.innerHTML = '<span class="loading"></span> İşleniyor...';
    
    // Remove loading state after form submission (this is just for UX, actual submission will redirect)
    setTimeout(() => {
        button.disabled = false;
        button.textContent = originalText;
    }, 2000);
}

// ===== Utility Functions =====
function enableSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

function autoResizeTextareas() {
    const textareas = document.querySelectorAll('textarea');
    
    textareas.forEach(textarea => {
        function autoResize() {
            this.style.height = 'auto';
            this.style.height = this.scrollHeight + 'px';
        }
        
        textarea.addEventListener('input', autoResize);
        autoResize.call(textarea);
    });
}

// ===== CSS Animations =====
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
    
    .is-invalid {
        animation: shake 0.5s ease-in-out;
    }
    
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
        20%, 40%, 60%, 80% { transform: translateX(5px); }
    }
`;
document.head.appendChild(style);

// ===== Utility Functions for Dynamic Content =====
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type}`;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        min-width: 300px;
        transform: translateX(100%);
        transition: transform 0.3s ease;
    `;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Animate out and remove
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 3000);
}

// ===== Export functions for global use =====
window.CVGenerator = {
    showNotification,
    addLoadingState,
    validateInput
}; 