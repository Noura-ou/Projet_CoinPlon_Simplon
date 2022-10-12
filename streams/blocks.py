from wagtail.core import blocks


class TitleBlock(blocks.StructBlock):

    text = blocks.CharBlock(
        required= True,
        help_text= "Text to display"


    )

    class Meta: #pour personnaliser la classe
        template = "streams/title_block.html"   #fichier HTML qui va representer ce blocks
        icon = "edit"
        label = "Titre"
        help_text = "Texte centré à afficher sur la page"

