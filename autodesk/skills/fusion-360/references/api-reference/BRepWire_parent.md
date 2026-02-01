# BRepWire.parent Property

Parent Object: [BRepWire](BRepWire.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWire.h>

## Description

Returns the parent BRepBody object that contains this wire.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWire\_var" is a variable referencing a BRepWire object. |

"bRepWire\_var" is a variable referencing a BRepWire object. ```` ``` #include <Fusion/BRep/BRepWire.h>  // Get the value of the property. Ptr<BRepBody> propertyValue = bRepWire_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBody](BRepBody.htm).

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