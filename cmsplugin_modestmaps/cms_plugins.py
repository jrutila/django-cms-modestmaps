from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import Map
from django.utils.translation import ugettext as _

class ModestMapsPlugin(CMSPluginBase):
    model = Map
    name = _("ModestMaps")
    render_template = "modestmaps.html"

    def render(self, context, instance, placeholder):
        context.update({
            'instance':instance, 
            'placeholder':placeholder, 
        })
        return context
    
plugin_pool.register_plugin(ModestMapsPlugin)
