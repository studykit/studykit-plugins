# BRepShells.item Method

Parent Object: [BRepShells](BRepShells.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepShells.h>

## Description

Function that returns the specified shell using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepShells\_var" is a variable referencing a [BRepShells](BRepShells.htm) object.```` ``` returnValue = bRepShells_var.item(index) ``` ```` |

"bRepShells\_var" is a variable referencing a [BRepShells](BRepShells.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepShell](BRepShell.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |