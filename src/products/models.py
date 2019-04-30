import random
import os
from django.db import models
from django.urls import reverse

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    title = instance.title
    new_filename = '{title}{random}'.format(title=title.replace(" ", ""), random=random.randint(1,599972678))
    print(new_filename)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{title}/{final_filename}".format(
            title=title.replace(" ", ""),
            final_filename=final_filename
            )

class ProductManager(models.Manager):
    def featured(self, slug):
        if slug == None :
            qs = self.get_queryset().filter(featured = True)
            if qs.count() >= 1:
                return qs
            else:
                return None
        else :
            qs = self.get_queryset().filter(slug=slug)
            qs = qs.filter(featured=True)
            if qs.count() == 1:
                return qs.first()
            else:
                return None

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get_by_slug(self, slug):
        qs = self.get_queryset().filter(slug=slug)
        if qs.count() == 1:
            return qs.first()
        return None

# Create your models here.
class Product(models.Model):
    title           = models.CharField(max_length=50)
    slug            = models.SlugField(blank=False,null=False,unique=True,max_length=20)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2,max_digits=19,default=1.99)
    image           = models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    featured        = models.BooleanField(default=False)

    objects = ProductManager()

    def get_absolute_url(self):
        if self.featured == True:
            return reverse("products:f_detail", kwargs={"slug":self.slug})
        else:
            return reverse("products:detail", kwargs={"slug":self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
