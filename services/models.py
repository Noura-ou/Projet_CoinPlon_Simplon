from django.db import models
from django.forms import ValidationError
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class ServicesListingPage(Page):
  # template = 'services/services/services_listing_page.html'
    subtitle = models.TextField(
        blank=True,
        max_length=500
    )
    content_panels = Page.content_panels + [
        FieldPanel("subtitle")
    ]


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # Add extra variables and return the updated context
        context['services'] = ServicePage.objects.live().public()
       # (import pudb; pu.db() ) #pour explorer les variable sur la ligne de commande
        return context
    
        # on va pouvoir récuperer les informations de service, .live pour prendre juste ce qui est publié, .object : pour recuperer ce qu on cree en service page#}

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

    def clean(self):
        super().clean()

        if self.internal_page and self.external_page :   #si les deux (lien interne et lien externe) renvoie un mesg d erreur
            raise ValidationError({
                'internal_page': ValidationError('SVP, Sélectionner un lien interne OU un lien externe'),
                'external_page': ValidationError('SVP, Sélectionner un lien interne OU un lien externe')
            })

        if not self.internal_page and not self.external_page :   #si no one (lien interne et lien externe) renvoie un mesg d erreur
            raise ValidationError({
                'internal_page': ValidationError('Vous devez avoir au moins sélectionner un lien interne ou externe'),
                'external_page': ValidationError('Vous devez avoir au moins sélectionner un lien interne ou externe')
            })