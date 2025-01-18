from django.shortcuts import render
from .models import CarouselSlide, FooterContent, GalleryImage

# Create your views here.

def index(request):
    slides = CarouselSlide.objects.all()
    footer_content = FooterContent.objects.first()
    return render(request, 'index.html', {
        'slides': slides,
        'footer_content': footer_content,
    })

def about(request):
    footer_content = FooterContent.objects.first()
    return render(request, 'about.html', { 'footer_content': footer_content })

def services(request):
    footer_content = FooterContent.objects.first()
    return render(request, 'services.html', {'footer_content': footer_content})

def gallery(request):
    footer_content = FooterContent.objects.first()
    gallery_images = GalleryImage.objects.all()  # Fetch all gallery images
    return render(request, 'gallery.html', {
        'footer_content': footer_content,
        'gallery_images': gallery_images
    })

def contact(request):
    footer_content = FooterContent.objects.first()
    return render(request, 'contact.html', { 'footer_content': footer_content })