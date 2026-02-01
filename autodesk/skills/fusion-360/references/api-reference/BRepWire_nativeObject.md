# BRepWire.nativeObject Property

Parent Object: [BRepWire](BRepWire.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWire.h>

## Description

The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWire\_var" is a variable referencing a BRepWire object. |

"bRepWire\_var" is a variable referencing a BRepWire object. ```` ``` #include <Fusion/BRep/BRepWire.h>  // Get the value of the property. Ptr<BRepWire> propertyValue = bRepWire_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepWire](BRepWire.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BrepWire Sample](BrepWireSample_Sample.htm) | BrepWires and BrepWire related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |