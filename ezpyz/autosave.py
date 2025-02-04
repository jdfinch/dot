
from ezpyz import file
import typing as T



class AutosavedFunction:

    def __init__(self, fn, format):
        self.fn = fn
        self.format = format

    def __call__(self, *args, save=None, load=None, **kwargs):
        if load and not save:
            return file.File(load).load()
        result = self.fn(*args, **kwargs)
        if save or save is None and load is None:
            self.format.save()
        return result


F = T.TypeVar('F')

def autosave(fn:F=None, *, format=None) -> F | AutosavedFunction:
    if fn is None:
        return lambda fn: autosave(fn, format=format)
    return AutosavedFunction(fn, format=format)




