from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class Blog(Page):
    
    template = 'blog/blog_page.html'

    blog_img = models.ForeignKey("wagtailimages.Image", blank=False, null=True, on_delete=models.SET_NULL, related_name="+")
    blog_opisanie_1 = models.CharField(max_length=100, blank=True, null=True)
    blog_opisanie_2 = models.CharField(max_length=100, blank=True, null=True)
    blog_opisanie_3 = models.CharField(max_length=100, blank=True, null=True)
    blog_opisanie_4 = models.CharField(max_length=100, blank=True, null=True)

    content_panels = Page.content_panels + [FieldPanel("blog_img"),
                                            FieldPanel("blog_opisanie_1"),
                                            FieldPanel("blog_opisanie_2"),
                                            FieldPanel("blog_opisanie_3"),
                                            FieldPanel("blog_opisanie_4")
                                            ]