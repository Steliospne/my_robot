# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from my_robot_driver/Buttons.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Buttons(genpy.Message):
  _md5sum = "a70f11db20213bb4fddba7dccd32ec5f"
  _type = "my_robot_driver/Buttons"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
bool reset
bool mode
bool stop
bool debug"""
  __slots__ = ['reset','mode','stop','debug']
  _slot_types = ['bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       reset,mode,stop,debug

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Buttons, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.reset is None:
        self.reset = False
      if self.mode is None:
        self.mode = False
      if self.stop is None:
        self.stop = False
      if self.debug is None:
        self.debug = False
    else:
      self.reset = False
      self.mode = False
      self.stop = False
      self.debug = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_4B().pack(_x.reset, _x.mode, _x.stop, _x.debug))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 4
      (_x.reset, _x.mode, _x.stop, _x.debug,) = _get_struct_4B().unpack(str[start:end])
      self.reset = bool(self.reset)
      self.mode = bool(self.mode)
      self.stop = bool(self.stop)
      self.debug = bool(self.debug)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_4B().pack(_x.reset, _x.mode, _x.stop, _x.debug))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 4
      (_x.reset, _x.mode, _x.stop, _x.debug,) = _get_struct_4B().unpack(str[start:end])
      self.reset = bool(self.reset)
      self.mode = bool(self.mode)
      self.stop = bool(self.stop)
      self.debug = bool(self.debug)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4B = None
def _get_struct_4B():
    global _struct_4B
    if _struct_4B is None:
        _struct_4B = struct.Struct("<4B")
    return _struct_4B
