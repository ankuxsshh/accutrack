from django.db import models

class CarouselSlide(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    heading = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading

class FooterContent(models.Model):
    address = models.TextField()
    email = models.EmailField(default="")
    phone_number = models.CharField(max_length=20, default="")

    def __str__(self):
        return "Footer Content"
    
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
    