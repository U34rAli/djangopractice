from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import django.dispatch

# Create your models here.

my_dispatch = django.dispatch.Signal()


class DateTimeMixin(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(DateTimeMixin):
    name = models.CharField(max_length=200, blank=False, unique=True)

    def __str__(self):
        return 'Company name: %s' % self.name

    class Meta:
        ordering = ['created_at']


class Product(DateTimeMixin):
    name = models.CharField(max_length=200, unique=True, blank=False)
    company = models.ForeignKey( Company, on_delete=models.CASCADE, related_name='products' )

    def __str__(self):
        return 'Product name: %s' % self.name


class Comment(DateTimeMixin):
    comment = models.CharField(max_length=1000, unique=True, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return 'Comment: %s' % self.comment


def my_callback(sender, **kwargs):
    print("Request finished!")



@receiver(pre_save, sender=Company)
def my_handler(sender, **kwargs):
    print("Model pre_saved")



class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline