from wagtail.contrib.modeladmin.options import ModelAdmin,modeladmin_register
from .models import Temoignage  #le point pour importer un modèle en local

@modeladmin_register               #decorateur à ma classe temoignage admin

# Register your models here.
class TemoignageAdmin(ModelAdmin) :
    model = Temoignage
    menu_label = "Temoignage"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False


# modeladmin_register(TemoignageAdmin)  #pour enregistrer cette classe