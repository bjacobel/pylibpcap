# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.31
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _pcap
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


__doc__ = _pcap.__doc__
for dltname, dltvalue in list(_pcap.DLT.items()):
  globals()[dltname] = dltvalue
del dltname, dltvalue


class pcapObject(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pcapObject, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pcapObject, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        import sys
        if int(sys.version[0])>='2':
            self.datalink.__func__.__doc__ = _pcap.pcapObject_datalink.__doc__
            self.fileno.__func__.__doc__ = _pcap.pcapObject_fileno.__doc__
            self.datalinks.__func__.__doc__ = _pcap.pcapObject_datalinks.__doc__
            self.major_version.__func__.__doc__ = _pcap.pcapObject_major_version.__doc__
            self.minor_version.__func__.__doc__ = _pcap.pcapObject_minor_version.__doc__
            self.getnonblock.__func__.__doc__ = _pcap.pcapObject_getnonblock.__doc__
            self.open_live.__func__.__doc__ = _pcap.pcapObject_open_live.__doc__
            self.dispatch.__func__.__doc__ = _pcap.pcapObject_dispatch.__doc__
            self.setnonblock.__func__.__doc__ = _pcap.pcapObject_setnonblock.__doc__
            self.stats.__func__.__doc__ = _pcap.pcapObject_stats.__doc__
            self.is_swapped.__func__.__doc__ = _pcap.pcapObject_is_swapped.__doc__
            self.open_dead.__func__.__doc__ = _pcap.pcapObject_open_dead.__doc__
            self.dump_open.__func__.__doc__ = _pcap.pcapObject_dump_open.__doc__
            self.next.__func__.__doc__ = _pcap.pcapObject_next.__doc__
            self.open_offline.__func__.__doc__ = _pcap.pcapObject_open_offline.__doc__
            self.snapshot.__func__.__doc__ = _pcap.pcapObject_snapshot.__doc__
            self.loop.__func__.__doc__ = _pcap.pcapObject_loop.__doc__
            self.setfilter.__func__.__doc__ = _pcap.pcapObject_setfilter.__doc__
        this = _pcap.new_pcapObject(*args)
        try: self.this.append(this)
        except: self.this = this
    def open_live(*args): return _pcap.pcapObject_open_live(*args)
    def open_dead(*args): return _pcap.pcapObject_open_dead(*args)
    def open_offline(*args): return _pcap.pcapObject_open_offline(*args)
    def dump_open(*args): return _pcap.pcapObject_dump_open(*args)
    def setnonblock(*args): return _pcap.pcapObject_setnonblock(*args)
    def getnonblock(*args): return _pcap.pcapObject_getnonblock(*args)
    def setfilter(*args): return _pcap.pcapObject_setfilter(*args)
    def loop(*args): return _pcap.pcapObject_loop(*args)
    def dispatch(*args): return _pcap.pcapObject_dispatch(*args)
    def next(*args): return _pcap.pcapObject_next(*args)
    def datalink(*args): return _pcap.pcapObject_datalink(*args)
    def datalinks(*args): return _pcap.pcapObject_datalinks(*args)
    def snapshot(*args): return _pcap.pcapObject_snapshot(*args)
    def is_swapped(*args): return _pcap.pcapObject_is_swapped(*args)
    def major_version(*args): return _pcap.pcapObject_major_version(*args)
    def minor_version(*args): return _pcap.pcapObject_minor_version(*args)
    def stats(*args): return _pcap.pcapObject_stats(*args)
    def fileno(*args): return _pcap.pcapObject_fileno(*args)
    __swig_destroy__ = _pcap.delete_pcapObject
    __del__ = lambda self : None;
pcapObject_swigregister = _pcap.pcapObject_swigregister
pcapObject_swigregister(pcapObject)

lookupdev = _pcap.lookupdev
findalldevs = _pcap.findalldevs
lookupnet = _pcap.lookupnet
aton = _pcap.aton
ntoa = _pcap.ntoa


