# BRepFaceDefinitions.item Method

Parent Object: [BRepFaceDefinitions](BRepFaceDefinitions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFaceDefinitions.h>

## Description

Function that returns the specified BRepFaceDefinition object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepFaceDefinitions\_var" is a variable referencing a [BRepFaceDefinitions](BRepFaceDefinitions.htm) object.```` ``` returnValue = bRepFaceDefinitions_var.item(index) ``` ```` |

"bRepFaceDefinitions\_var" is a variable referencing a [BRepFaceDefinitions](BRepFaceDefinitions.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepFaceDefinition](BRepFaceDefinition.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |