from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from decimal import *
import sys

class Map(CMSPlugin):
  title = models.CharField(_("title"), max_length=50)
  zoom = models.IntegerField(_("zoom level"), blank=True, null=True)
  lat = models.DecimalField(_('latitude'), max_digits=10, decimal_places=6, null=True, blank=True, 
    help_text=_('Use latitude & longitude to fine tune the map possiton.'))
  lng = models.DecimalField(_('longitude'), max_digits=10, decimal_places=6, null=True, blank=True)

  def __unicode__(self):
    return u"%s" % (self.title)
