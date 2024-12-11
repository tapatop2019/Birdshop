from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class Mistake(Page):

    template = "mistake/mistake_page.html"

    mistake_opisanie_1 = models.CharField(max_length=100, null=True, blank= True)
    mistake_opisanie_2 = models.CharField(max_length=100, null=True, blank= True)
    mistake_opisanie_3 = models.CharField(max_length=100, null=True, blank= True)

    content_panels = Page.content_panels + [FieldPanel("mistake_opisanie_1"),
                                            FieldPanel("mistake_opisanie_2"),
                                            FieldPanel("mistake_opisanie_3")
                                            ]