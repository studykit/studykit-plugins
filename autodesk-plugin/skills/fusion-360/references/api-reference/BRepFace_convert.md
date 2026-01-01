# BRepFace.convert Method

Parent Object: [BRepFace](BRepFace.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFace.h>

## Description

Creates a new body where this face and its edges are converted to different types of geometry based on the input options.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepFace\_var" is a variable referencing a [BRepFace](BRepFace.htm) object.```` ``` returnValue = bRepFace_var.convert(options) ``` ```` |

"bRepFace\_var" is a variable referencing a [BRepFace](BRepFace.htm) object.  ```` ``` #include <Fusion/BRep/BRepFace.h>  returnValue = bRepFace_var->convert(options); ``` ```` |

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