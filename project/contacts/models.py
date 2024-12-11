from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class Contacts(Page):

    template = "contact\contact_page.html"
    
    contact_zagolovok= models.CharField(max_length=100, null=True, blank=True)
    contact_einfo= models.CharField(max_length=100, null=True, blank=True)
    contact_esupport= models.CharField(max_length=100, null=True, blank=True)
    contact_phone_1= models.CharField(max_length=100, null=True, blank=True)
    contact_phone_2= models.CharField(max_length=100, null=True, blank=True)
    contact_numberstreet= models.CharField(max_length=100, null=True, blank=True)
    contact_street= models.CharField(max_length=100, null=True, blank=True)
    contact_text_1= models.CharField(max_length=100, null=True, blank=True)
    contact_text_2= models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [FieldPanel("contact_zagolovok"),
                                            FieldPanel("contact_einfo"),
                                            FieldPanel("contact_esupport"),
                                            FieldPanel("contact_phone_1"),
                                            FieldPanel("contact_phone_2"),
                                            FieldPanel("contact_numberstreet"),
                                            FieldPanel("contact_street"),
                                            FieldPanel("contact_text_1"),
                                            FieldPanel("contact_text_2")
                                            ]