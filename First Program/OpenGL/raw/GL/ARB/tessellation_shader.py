'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_tessellation_shader'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_ARB_tessellation_shader',error_checker=_errors._error_checker)
GL_CCW=_C('GL_CCW',0x0901)
GL_CW=_C('GL_CW',0x0900)
GL_EQUAL=_C('GL_EQUAL',0x0202)
GL_FRACTIONAL_EVEN=_C('GL_FRACTIONAL_EVEN',0x8E7C)
GL_FRACTIONAL_ODD=_C('GL_FRACTIONAL_ODD',0x8E7B)
GL_ISOLINES=_C('GL_ISOLINES',0x8E7A)
GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS=_C('GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS',0x8E1E)
GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS=_C('GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS',0x8E1F)
GL_MAX_PATCH_VERTICES=_C('GL_MAX_PATCH_VERTICES',0x8E7D)
GL_MAX_TESS_CONTROL_INPUT_COMPONENTS=_C('GL_MAX_TESS_CONTROL_INPUT_COMPONENTS',0x886C)
GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS=_C('GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS',0x8E83)
GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS=_C('GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS',0x8E81)
GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS=_C('GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS',0x8E85)
GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS=_C('GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS',0x8E89)
GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS=_C('GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS',0x8E7F)
GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS=_C('GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS',0x886D)
GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS=_C('GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS',0x8E86)
GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS=_C('GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS',0x8E82)
GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS=_C('GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS',0x8E8A)
GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS=_C('GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS',0x8E80)
GL_MAX_TESS_GEN_LEVEL=_C('GL_MAX_TESS_GEN_LEVEL',0x8E7E)
GL_MAX_TESS_PATCH_COMPONENTS=_C('GL_MAX_TESS_PATCH_COMPONENTS',0x8E84)
GL_PATCHES=_C('GL_PATCHES',0x000E)
GL_PATCH_DEFAULT_INNER_LEVEL=_C('GL_PATCH_DEFAULT_INNER_LEVEL',0x8E73)
GL_PATCH_DEFAULT_OUTER_LEVEL=_C('GL_PATCH_DEFAULT_OUTER_LEVEL',0x8E74)
GL_PATCH_VERTICES=_C('GL_PATCH_VERTICES',0x8E72)
GL_QUADS=_C('GL_QUADS',0x0007)
GL_TESS_CONTROL_OUTPUT_VERTICES=_C('GL_TESS_CONTROL_OUTPUT_VERTICES',0x8E75)
GL_TESS_CONTROL_SHADER=_C('GL_TESS_CONTROL_SHADER',0x8E88)
GL_TESS_EVALUATION_SHADER=_C('GL_TESS_EVALUATION_SHADER',0x8E87)
GL_TESS_GEN_MODE=_C('GL_TESS_GEN_MODE',0x8E76)
GL_TESS_GEN_POINT_MODE=_C('GL_TESS_GEN_POINT_MODE',0x8E79)
GL_TESS_GEN_SPACING=_C('GL_TESS_GEN_SPACING',0x8E77)
GL_TESS_GEN_VERTEX_ORDER=_C('GL_TESS_GEN_VERTEX_ORDER',0x8E78)
GL_TRIANGLES=_C('GL_TRIANGLES',0x0004)
GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER=_C('GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER',0x84F0)
GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER=_C('GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER',0x84F1)
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glPatchParameterfv(pname,values):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glPatchParameteri(pname,value):pass
