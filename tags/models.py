from django.db import models
# from store.models import Product
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.


class Tag(models.Model):
    labels = models.CharField(max_length=255)

    def __str__(self):
        return self.labels


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # what tage applied to what object
    # poor way of implementing what tag applied to
    # what opject like Product you need to import it on the top
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # A generic way to identify tag items
    # To do so, we need to attributes
    # 1- Type(product, video, artice,...)
    # 2- ID of that object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
