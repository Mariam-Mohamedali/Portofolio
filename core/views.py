from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, Certificate, ContactMessage


def home(request):
    featured_projects = Project.objects.filter(featured=True)[:3]
    skills = Skill.objects.all()
    certificates = Certificate.objects.all()[:3]
    return render(request, 'core/home.html', {
        'featured_projects': featured_projects,
        'skills': skills,
        'certificates': certificates,
        'project_count': Project.objects.count(),
        'cert_count': Certificate.objects.count(),
        'skill_count': Skill.objects.count(),
    })


def about(request):
    skills = Skill.objects.all()
    skill_categories = {
        'language': skills.filter(category='language'),
        'backend': skills.filter(category='backend'),
        'frontend': skills.filter(category='frontend'),
        'database': skills.filter(category='database'),
        'tools': skills.filter(category='tools'),
    }
    return render(request, 'core/about.html', {
        'skills': skills,
        'skill_categories': skill_categories,
    })


def projects(request):
    category = request.GET.get('category', 'all')
    all_projects = Project.objects.all()
    if category != 'all':
        all_projects = all_projects.filter(category=category)
    return render(request, 'core/projects.html', {
        'projects': all_projects,
        'active_category': category,
    })


def certificates(request):
    certs = Certificate.objects.all()
    return render(request, 'core/certificates.html', {'certificates': certs})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and subject and message:
            try:
                ContactMessage.objects.create(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message
                )
            except Exception as e:
                print("Could not save to DB:", e)
            
            # Send Email Notification synchronously (safer for serverless)
            from django.core.mail import send_mail
            from django.conf import settings
            
            try:
                send_mail(
                    subject=f"New Portfolio Message: {subject}",
                    message=f"You have a new message from {name} ({email}):\n\n{message}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['mariammohamedali127@gmail.com'],
                    fail_silently=True,
                )
            except Exception:
                pass
            
            messages.success(request, 'Message sent successfully! I\'ll get back to you soon. 🚀')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'core/contact.html')
