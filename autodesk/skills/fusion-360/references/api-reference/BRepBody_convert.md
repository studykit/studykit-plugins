# BRepBody.convert Method

Parent Object: [BRepBody](BRepBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBody.h>

## Description

Creates a new body where the faces and edges are converted to different types of geometry based on the input options. This is particularly useful when you need a body made up entirely of NURBS surfaces.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBody\_var" is a variable referencing a [BRepBody](BRepBody.htm) object.```` ``` returnValue = bRepBody_var.convert(options) ``` ```` |

"bRepBody\_var" is a variable referencing a [BRepBody](BRepBody.htm) object.  ```` ``` #include <Fusion/BRep/BRepBody.h>  returnValue = bRepBody_var->convert(options); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepBody](BRepBody.htm) | Returns the new converted body or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| options | [BRepConvertOptions](BRepConvertOptions.htm) | Input options that define how the conversion should be done. These are bitwise options so they can be combined. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |