from matplotlib import rcParams, rcdefaults
#standardize mpl setup
rcdefaults()
rcParams['interactive'] = False  # prevents extra window from popping up

from .histogram_client import HistogramClient
from .image_client import ImageClient
from .scatter_client import ScatterClient
