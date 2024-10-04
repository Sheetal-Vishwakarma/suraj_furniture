from django.db import models

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from PIL import Image as PILImage
import io

# Create your models here.
class Contactus(models.Model):
    name = models.TextField()
    email = models.EmailField(null=True)
    subject = models.TextField(null=True)
    message = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)    
    class Meta:
        db_table ="contact_us"

class Newsletter(models.Model):
    TYPE_CHOICES = (
        ('0', '0'),
        ('1','1')
        )
    email = models.EmailField(null=True)
    is_subscribed = models.CharField(max_length=5,choices=TYPE_CHOICES,default='0')
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)    
    class Meta:
        db_table ="newsletter"        

class Gallery(models.Model):
    TYPE_CHOICES = (
        ('Sofa and Bed', 'Sofa and Bed'),
        ('Modular Kitchen','Modular Kitchen'),
        ('Table and Chairs','Table and Chairs'),
        ('Cupboard','Cupboard'),
        ('Wall Decore','Wall Decore'),
        ('TV Cabinet','TV Cabinet'),
        ('Door','Door'),
        ('Wooden Art','Wooden Art'),
        ('Other','Other')        
        )
    type = models.CharField(max_length=255,choices=TYPE_CHOICES,default='Sofa and Bed')
    image_name = models.ImageField(upload_to='gallery/',blank=True,max_length=2024)
    title = models.CharField(max_length=255,null=True)
    status = models.SmallIntegerField(null=True,default=1)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = "gallery"

    def save(self, *args, **kwargs):
        if self.image_name:
            # Open the uploaded image
            img = PILImage.open(self.image_name)

            # Resize the image
            img = img.resize((1024, 768), PILImage.LANCZOS)

            # Save it to a BytesIO object
            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=85)  # You can choose 'PNG' or adjust quality
            img_file = ContentFile(img_io.getvalue(), name=self.image_name.name)

            # Update the image_name field
            self.image_name = img_file

        super().save(*args, **kwargs) 

class Testimonial(models.Model):
    name = models.CharField(max_length=255,null=True)
    profile_image = models.CharField(max_length=255,null=True)
    designation = models.CharField(max_length=255,null=True)
    rating = models.SmallIntegerField(default=4)
    description = models.TextField(blank=True,null=True)
    status = models.BooleanField(default=True,db_comment='0:Inactive, 1:Active')
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = "testimonial"    
    def __str__(self):
      return "Name: {}".format(self.name)

# class Practice(models.Model):
#     title = models.CharField(max_length=200)
#     name = models.CharField(max_length=255)
#     identifier = models.CharField(max_length=15)
#     status = models.BooleanField(default=1)

#     def save(self, *args, **kwargs):
#         if self.id is None:  # Adding of a new instance
#             # let's say we compare instances by `title`
#             # you can use other fields for the comparison
#             possible_old_instance = Practice.objects.filter(title__iexact=self.title)                                            
#             if possible_old_instance.exists():
#                 print('update existing data')
#                 existing_model = possible_old_instance.first()                
#                 existing_model.title = self.title
#                 existing_model.name = self.name
#                 existing_model.status = 1
#                 existing_model.save()
#                 # Nothing happens, we don't call save() method
#             else:
#                 print('------------ field data ------')
#                 print(f"Name : {self.name}")
#                 print(f"Title : {self.title}")
#                 print(f"Identifier : {self.identifier}")
#                 print('------------ field data ------')
#                 # in case the Model doesn't exist
#                 super(Practice, self).save(*args, **kwargs)
#         else:
#             super(Practice, self).save(*args, **kwargs)