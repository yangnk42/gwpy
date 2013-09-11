
"""Layers for GWpy Plot objects

Each layer represents a data set added to a plot, e.g. a line or some
scatter points. The LayerCollection is attached to the plot to allow
recording and extraction of individual layers in complex plots.
"""

from .. import version
__author__ = "Duncan Macleod <duncan.macleod@ligo.org>"
__version__ = version.version

try:
    from collections import OrderedDict
except ImportError:
    from astropy.utils import OrderedDict


class LayerCollection(OrderedDict):
    """Object recording the plotting layers on a figure
    """
    LAYER_TYPES = ['Line2D', 'PathCollection']
    def count(self, type_=None):
        if type_:
            if type_ not in self.LAYER_TYPES:
                raise ValueError("No layer type '%s' defined for this "
                                 "Collection" % type_)
            return sum(l for l in self.viewvalues() if
                       l.__class__.__name__ == type_)
        else:
            return len(self)

    def add(self, layer):
        self[layer.get_label()] = layer

    @property
    def colorlayer(self):
        """The first mappable layer available for use in a Colorbar
        """
        for layer in self.viewvalues():
            if layer.__class__.__name__ in ['PathCollection']:
                return layer
        raise ValueError("No mappable layers in this Collection")