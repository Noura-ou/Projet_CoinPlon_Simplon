# from email.policy import default
from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
import lorem

class FlexPage(Page):
   # template = 'flex/flex_page.html'
    text = models.TextField(
        max_length=600,
        null=True,
        blank=True,
        default=lorem.paragraph()
    )
    content_panels = Page.content_panels + [FieldPanel('text')]

    class Meta :
        verbose_name = "Page divers"
        verbose_name_plural = "Pages divers"

    
    

    


