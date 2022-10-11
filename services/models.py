from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class ServicesListingPage(Page):
    subtitle = models.TextField(
        blank=True,
        max_length=500
    )
    content_panels = Page.content_panels + [
        FieldPanel("subtitle")
    ]

class ServicePage(Page):
    description = models.TextField(
        blank=True,
        max_length=500
    )

    internal_page = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name="+",
        help_text="Sélectionner une page interne",
        on_delete=models.SET_NULL
    )

    external_page = models.URLField(blank=True)

    button_text = models.CharField(blank=True, max_length=50)

    service_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text="Choisir une image pour ce service",
        related_name="+"
    )

    #faire apparaitre les trucs dans la page web child

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("internal_page"),
        FieldPanel("external_page"),
        FieldPanel("button_text"),
        FieldPanel("service_image"),
    ]