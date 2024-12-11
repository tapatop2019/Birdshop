
from django.db import models
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey




 

class caruselImages(Orderable):
    # Orderable позволяет создавать карусель
    
    page = ParentalKey("home.HomePage", related_name="carusel_images")
    
    carusel_image=models.ForeignKey("wagtailimages.Image", blank = False, null = True,on_delete=models.SET_NULL, related_name="+")

    panels=[FieldPanel("carusel_image")]

class HomePage(Page):
    template="home/home_page.html" 

    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_title_2 = models.CharField(max_length=100, blank=False, null=True)
    banner_title_3 = models.CharField(max_length=100, blank=True , null=True)
    banner_title_4 = models.CharField(max_length=100, blank=True , null=True)
    content_panels = Page.content_panels + [FieldPanel("banner_title"), 
                                            FieldPanel("banner_title_2"),
                                            FieldPanel("banner_title_3"),
                                            FieldPanel("banner_title_4"),
                                            InlinePanel("carusel_images")]
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs) # берем данные из конетекста
        context["products"] = Page.objects.get( slug = 'products') # мы берем обьекты по слагу ведь слаг это уникальный индиыикатор url
        context["about"] = Page.objects.get( slug='abouttt' )
        context["products"] = Page.objects.get( slug='products')
        context["store"] = Page.objects.get(slug='store')
        
        return context
 