from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField # Para las imagenes

from apps.category.models import Category

def blog_thumbnail_directory(instance, filename):
    return f'blog/{instance.title}/{filename}' # funcion que indica el directorio en media/blog(automatico)

class Post(models.Model):

    title =         models.CharField(max_length=255)
    slug =          models.SlugField(max_length=255, unique=True)
    thumbnail =     models.ImageField(upload_to=blog_thumbnail_directory) # upload_to donde la subimos
    description =   models.TextField(max_length=255) # Description small
    content =       RichTextUploadingField() # Texto enriquesido esto depende de la config que le dimos
    published =     models.DateTimeField(default=timezone.now)
    views =         models.IntegerField(default=0, blank=True)
    time_red =      models.IntegerField()

    category =      models.ForeignKey(Category, on_delete=models.PROTECT) # Si se borra la categoría el post no y <<vs>>

    class Meta:
        ordering = ('-published', ) # Con esto tomamos el mas nuevo

    def __str__(self): # Como lo queremos ver
        return self.title

    def get_view_count(self):
        views = ViewCount.objects.filter(post = self).count()
        return views

class ViewCount(models.Model):

    post =          models.ForeignKey(Post, related_name='blogpost_view_count', on_delete=models.CASCADE)
    ip_address =    models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ip_address}"