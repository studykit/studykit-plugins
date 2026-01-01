# BRepWires.item Method

Parent Object: [BRepWires](BRepWires.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWires.h>

## Description

Function that returns the specified wire using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWires\_var" is a variable referencing a [BRepWires](BRepWires.htm) object.```` ``` returnValue = bRepWires_var.item(index) ``` ```` |

"bRepWires\_var" is a variable referencing a [BRepWires](BRepWires.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepWire](BRepWire.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

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