from . import kusocket as socket

from . import math
from . import file
from . import manage
from . import print

_DoNotImport = {}

def ImportOtherSubmodule(Submodule):
    if Submodule.lower() in _DoNotImport:
        _DoNotImport[Submodule]()
    else:
        print("No submodule '" + Submodule.capitalize() + "'")

def _DefineSubmodule(Name, Func):
    _DoNotImport[Name] = Func

def _ImportYoutube():
    from . import youtube

_DefineSubmodule("youtube", _ImportYoutube)
