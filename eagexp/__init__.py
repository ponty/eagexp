import logging
from eagexp.about import __version__

USE_DISPLAY = 0
try:
    from pyvirtualdisplay.display import Display
    USE_DISPLAY = 1

except:
    import warnings
    warnings.warn(
        'pyvirtualdisplay was not found, no background GUI work is possible')


log = logging.getLogger(__name__)
log.debug('version=%s', __version__)

