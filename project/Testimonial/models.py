from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class Testimonial(Page):

    template = 'testimonial/testimonial_page.html'

    testimonial_opisanie_1 = models.CharField(max_length=100, null=True, blank= True)
    testimonial_opisanie_2 = models.CharField(max_length=100, null=True, blank= True)
    testimonial_opisanie_3 = models.CharField(max_length=100, null=True, blank= True)
    testimonial_opisanie_4 = models.CharField(max_length=100, null=True, blank= True)
    testimonial_opisanie_5 = models.CharField(max_length=100, null=True, blank= True)
    testimonial_opisanie_6 = models.CharField(max_length=100, null=True, blank= True)
    testimonial_opisanie_7 = models.CharField(max_length=100, null=True, blank= True)
    content_panels = Page.content_panels + [FieldPanel("testimonial_opisanie_1"),
                                            FieldPanel("testimonial_opisanie_2"),
                                            FieldPanel("testimonial_opisanie_3"),
                                            FieldPanel("testimonial_opisanie_4"),
                                            FieldPanel("testimonial_opisanie_5"),
                                            FieldPanel("testimonial_opisanie_6"),
                                            FieldPanel("testimonial_opisanie_7")
                                            ]