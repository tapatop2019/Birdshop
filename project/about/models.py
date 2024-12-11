from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class About(Page):
    template = "about/about_page.html"

    about_banner_title = models.CharField (max_length=100, blank=True, null = False)
    about_zaglavtext = models.CharField (max_length=100, blank = True, null =False )
    about_opisanie_1 = models.CharField (max_length=100, blank=True, null = False)
    about_opisanie_2 = models.CharField (max_length=100, blank=True, null = False)
    about_opisanie_3 = models.CharField (max_length=100, blank=True, null =  False)
    about_opisanie_4 = models.CharField (max_length=100, blank=True, null =  False)
    about_picture_1 = models.ForeignKey ("wagtailimages.Image",blank=True, null=True,on_delete=models.SET_NULL, related_name="+")
    about_picture_2 = models.ForeignKey ("wagtailimages.Image",blank=True, null=True,on_delete=models.SET_NULL, related_name="+")
    about_picture_3 = models.ForeignKey ("wagtailimages.Image",blank=True, null=True,on_delete=models.SET_NULL, related_name="+")
    about_picture_4 = models.ForeignKey ("wagtailimages.Image",blank=True, null=True,on_delete=models.SET_NULL, related_name="+")
    about_picture_5 = models.ForeignKey ("wagtailimages.Image",blank=True, null=True,on_delete=models.SET_NULL, related_name="+")
    about_picture_6 = models.ForeignKey ("wagtailimages.Image",blank=True, null=True,on_delete=models.SET_NULL, related_name="+")  

    content_panels= Page.content_panels + [FieldPanel("about_banner_title"), 
                                           FieldPanel("about_zaglavtext"),
                                           FieldPanel("about_opisanie_1"),
                                           FieldPanel("about_opisanie_2"),
                                           FieldPanel("about_opisanie_3"),
                                           FieldPanel("about_opisanie_4"),
                                           FieldPanel("about_picture_1"),
                                           FieldPanel("about_picture_2"),
                                           FieldPanel("about_picture_3"),
                                           FieldPanel("about_picture_4"),
                                           FieldPanel("about_picture_5"),
                                           FieldPanel("about_picture_6")
                                           ]

