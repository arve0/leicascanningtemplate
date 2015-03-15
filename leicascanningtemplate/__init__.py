__author__ = 'Arve Seljebu'
__email__ = 'arve.seljebu@gmail.com'
from os.path import join, dirname
__version__ = open(join(dirname(__file__), 'VERSION')).read().strip()

from .template import ScanningTemplate

__all__ = ['ScanningTemplate']
