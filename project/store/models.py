from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class Store(Page):
    template ="store/store_page.html"
    
    store_zagolovok = models.CharField(max_length=100, blank = True, null = True)
    store_podzagolovok = models.CharField(max_length=100, blank = True, null = True)
    store_opisanie_1 = models.CharField(max_length=100, blank = True, null = True)
    store_opisanie_2 = models.CharField(max_length=100, blank = True, null = True)
    store_opisanie_3 = models.CharField(max_length=100, blank = True, null = True)
    store_opisanie_4 = models.CharField(max_length=100, blank = True, null = True)
    store_opisanie_5 = models.CharField(max_length=100, blank = True, null = True)
    store_opisanie_6 = models.CharField(max_length=100, blank = True, null = True)

    store_pic_1 = models.ForeignKey("wagtailimages.Image", blank = True, null=True, on_delete=models.SET_NULL, related_name="+")
    store_pic_2 = models.ForeignKey("wagtailimages.Image", blank = True, null=True, on_delete=models.SET_NULL, related_name="+")
    store_pic_3 = models.ForeignKey("wagtailimages.Image", blank = True, null=True, on_delete=models.SET_NULL, related_name="+")

    content_panels= Page.content_panels + [FieldPanel("store_zagolovok"),
                                           FieldPanel("store_podzagolovok"),
                                           FieldPanel("store_opisanie_1"),
                                           FieldPanel("store_opisanie_2"),
                                           FieldPanel("store_opisanie_3"),
                                           FieldPanel("store_opisanie_4"),
                                           FieldPanel("store_opisanie_5"),
                                           FieldPanel("store_opisanie_6"),
                                           FieldPanel("store_pic_1"),
                                           FieldPanel("store_pic_2"),
                                           FieldPanel("store_pic_3")]   
# Create your models here.
