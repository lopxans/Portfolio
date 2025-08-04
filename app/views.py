from django.shortcuts import render, redirect, get_object_or_404
from .form import ContactForm
from .models import *
from datetime import *
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

# About Page
def about(request):
    return render(request, 'app/about.html')

# Contact Page
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('contact')
    else:     
        form = ContactForm()
    data = Contact.objects.all()
    return render(request, 'app/contact.html', {'forms': form, 'data': data})

def contact_view(request):
    data = Contact.objects.filter(is_delete=False)
    delete_data = Contact.objects.filter(is_delete=True)
    return render(request, 'app/contact_view.html', {'contacts': data, 'delete_data': delete_data})

def recycle_contact(request):
    data = Contact.objects.filter(is_delete=True)
    threshold =  timezone.now() - timedelta(days=30)
    expired = Contact.objects.filter(is_delete=True, deleted_time__lt=threshold)
    
    deleted_count = expired.count()
    if deleted_count > 0:
        expired.delete()
    else:
        print("File is permanent deleted due to it's expired date. ")
    return render(request, 'app/recycle_contact.html', {'contacts': data})

def soft_delete_contact(request, id):
    data = Contact.objects.get(id=id)
    data.is_delete = True
    data.deleted_time = timezone.now() 
    data.save()
    return redirect('contact_view')

def hard_delete_contact(request, id):
    Contact.objects.get(id=id).delete()
    return redirect('recycle_contact')

def restore_contact(request, id):
    data = Contact.objects.get(id=id)
    data.is_delete = False
    data.save()
    return redirect('recycle_contact')

def restore_all_contact(request):
    Contact.objects.filter(is_delete=True).update(is_delete=False)
    return redirect('recycle_contact')

def clear_all_contact(request):
    Contact.objects.filter(is_delete=True).delete()
    return redirect('recycle_contact')
    
# Certificate Page
def certificate(request):
    certificate = Certificate.objects.filter(is_delete=False)
    data = Certificate.objects.filter(is_delete=True)
    return render(request, 'app/certificate.html', {'Certificates': certificate, 'data': data})

def certificate_form(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        title = request.POST.get('title')
        description = request.POST.get('description')
        issued_date = request.POST.get('issued_date')
        
        Certificate.objects.create(
            image = image,
            title = title,
            description = description,
            issued_date = issued_date,
        )
        return redirect('certificate')
        
    return render(request, 'app/certificate_form.html')

def recycle_certificate(request):
    data = Certificate.objects.filter(is_delete=True)
    threshold = timezone.now() - timedelta(days=30)
    expired = Certificate.objects.filter(is_delete=True, deleted_time__lt=threshold)
    
    deleted_count = expired.count()
    if deleted_count > 0:
        expired.delete()
    else:
        print("Empty")
        
    return render(request, 'app/recycle_certificate.html', {'certificates': data})

def certificate_soft_delete(request, id):
    data = Certificate.objects.get(id=id)
    data.is_delete = True
    data.deleted_time = timezone.now()
    data.save()
    return redirect('certificate')

def hard_delete_cert(request, id):
    certificate =  Certificate.objects.get(id = id)
    certificate.delete()
    return redirect('recycle_certificate')

def clear_all_cert(request):
    certificate =  Certificate.objects.filter(is_delete=True)
    certificate.delete()
    return redirect('recycle_certificate')

def restore_cert(request, id):
    data =  Certificate.objects.get(id=id)
    data.is_delete = False
    data.save()
    return redirect('recycle_certificate')

def restore_all_cert(request):
    Certificate.objects.filter(is_delete=True).update(is_delete=False)
    return redirect('recycle_certificate')

def edit_certificate(request, id):
    data = Certificate.objects.get(id=id)
    
    if request.method == "POST":
        data.image = request.FILES.get('image')
        data.title = request.POST.get('title')
        data.description = request.POST.get('description')
        data.issued_date = request.POST.get('issued_date')
        data.save()
        
        return redirect('certificate')
    return render(request, 'app/edit_certificate.html', {'data': data})

# Project Page
def project(request):
    project = Project.objects.filter(is_delete=False)
    data = Project.objects.filter(is_delete=True)
    return render(request, 'app/project.html', {'projects': project, 'data': data})

def project_form(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        title = request.POST.get('title')
        description = request.POST.get('description')
        link = request.POST.get('link')
        
        Project.objects.create(
            image = image,
            title = title,
            description = description,
            link = link,
        )
        
        return redirect('project')
    return render(request, 'app/project_form.html')

def recycle_project(request):
    data = Project.objects.filter(is_delete=True)
    threshold = timezone.now() - timedelta(days=30)
    expired = Project.objects.filter(is_delete=True, deleted_time__lt=threshold)
    
    deleted_count = expired.count()
    if deleted_count > 0:
        expired.delete()
    else:
        print("Empty")
        
    return render(request, 'app/recycle_project.html', {'projects': data})

def project_soft_delete(request, id):
    data = get_object_or_404(Project, id=id)
    data.is_delete = True
    data.deleted_time = timezone.now()
    data.save()
    return redirect('project')

def project_hard_delete(request, id):
    certificate =  Project.objects.get(id = id)
    certificate.delete()
    return redirect('recycle_project')

def project_clear_all(request):
    Project.objects.filter(is_delete=True).delete()
    
    return redirect('recycle_project')

def project_restore(request, id):
    data =  Project.objects.get(id = id)
    data.is_delete = False
    data.save()
    return redirect('recycle_project')

def project_restore_all(request):
    Project.objects.filter(is_delete=True).update(is_delete=False)
    return redirect('recycle_project')

def edit_project(request, id):
    data = Project.objects.get(id=id)
    if request.method == "POST":
        data.image = request.FILES.get('image')
        data.title = request.POST.get('title')
        data.description = request.POST.get('description')
        data.link = request.POST.get('link')
        data.save()
        
        return redirect('project')
    
    return render(request, 'app/edit_project.html', {'data': data})