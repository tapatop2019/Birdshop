from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class Features(Page):

    template = 'features/features_page.html'

    features_opisanie_1 = models.CharField(max_length=100, null=True, blank= True)
    features_opisanie_2 = models.CharField(max_length=100, null=True, blank= True)
    features_opisanie_3 = models.CharField(max_length=100, null=True, blank= True)
    features_opisanie_4 = models.CharField(max_length=100, null=True, blank= True)
    features_opisanie_5 = models.CharField(max_length=100, null=True, blank= True)
    features_opisanie_6 = models.CharField(max_length=100, null=True, blank= True)

    content_panels = Page.content_panels + [FieldPanel("features_opisanie_1"),
                                            FieldPanel("features_opisanie_2"),
                                            FieldPanel("features_opisanie_3"),
                                            FieldPanel("features_opisanie_4"),
                                            FieldPanel("features_opisanie_5"),
                                            FieldPanel("features_opisanie_6")]