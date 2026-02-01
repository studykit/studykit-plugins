# BRepVertex.nativeObject Property

Parent Object: [BRepVertex](BRepVertex.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepVertex.h>

## Description

The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepVertex\_var" is a variable referencing a BRepVertex object. |

"bRepVertex\_var" is a variable referencing a BRepVertex object. ```` ``` #include <Fusion/BRep/BRepVertex.h>  // Get the value of the property. Ptr<BRepVertex> propertyValue = bRepVertex_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepVertex](BRepVertex.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |