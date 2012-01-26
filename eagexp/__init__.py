'''
https://github.com/ponty/eagexp
'''
import logging

USE_DISPLAY = 0
try:
    from pyvirtualdisplay.display import Display
    USE_DISPLAY = 1

except:
    import warnings
    warnings.warn('pyvirtualdisplay was not found, no background GUI work is possible')



__version__ = '0.0.3'

log = logging.getLogger(__name__)
log.debug('version=' + __version__)
