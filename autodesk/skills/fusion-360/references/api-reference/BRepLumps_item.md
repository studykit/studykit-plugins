# BRepLumps.item Method

Parent Object: [BRepLumps](BRepLumps.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLumps.h>

## Description

Function that returns the specified lump using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLumps\_var" is a variable referencing a [BRepLumps](BRepLumps.htm) object.```` ``` returnValue = bRepLumps_var.item(index) ``` ```` |

"bRepLumps\_var" is a variable referencing a [BRepLumps](BRepLumps.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepLump](BRepLump.htm) | Returns the specified item or null if an invalid index was specified. |

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