from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class Products(Page):
    template="products/products_page.html"
    max_count = 1

    products_zagolovok = models.CharField(max_length=100, blank=True, null=False)
    products_opisanie_1 = models.CharField(max_length=100, blank=True, null=False)
    products_opisanie_2 = models.CharField(max_length=100, blank=True, null=False)
    products_opisanie_3 = models.CharField(max_length=100, blank=True, null=False)
    products_opisanie_4 = models.CharField(max_length=100, blank=True, null=False)
    products_opisanie_5 = models.CharField(max_length=100, blank=True, null=False)
    products_opisanie_6 = models.CharField(max_length=100, blank=True, null=False)
    products_opisanie_7 = models.CharField(max_length=100, blank=True, null=False)
    products_opisanie_8 = models.CharField(max_length=100, blank=True, null=False)

    products_picture_1 = models.ForeignKey("wagtailimages.Image", blank=True, null=True, on_delete=models.SET_NULL, related_name="+")
    products_picture_2 = models.ForeignKey("wagtailimages.Image", blank=True, null=True, on_delete=models.SET_NULL, related_name="+")
    products_picture_3 = models.ForeignKey("wagtailimages.Image", blank=True, null=True, on_delete=models.SET_NULL, related_name="+")
    products_picture_4 = models.ForeignKey("wagtailimages.Image", blank=True, null=True, on_delete=models.SET_NULL, related_name="+")
    
    content_panels=Page.content_panels +[FieldPanel("products_zagolovok"),
                                         FieldPanel("products_opisanie_1"),
                                         FieldPanel("products_opisanie_2"),
                                         FieldPanel("products_opisanie_3"),
                                         FieldPanel("products_opisanie_4"),
                                         FieldPanel("products_opisanie_5"),
                                         FieldPanel("products_opisanie_6"),
                                         FieldPanel("products_opisanie_7"),
                                         FieldPanel("products_opisanie_8"),
                                         FieldPanel("products_picture_1"),
                                         FieldPanel("products_picture_2"),
                                         FieldPanel("products_picture_3"),
                                         FieldPanel("products_picture_4")]
    
    
