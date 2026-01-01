# BRepCoEdgeDefinitions.item Method

Parent Object: [BRepCoEdgeDefinitions](BRepCoEdgeDefinitions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdgeDefinitions.h>

## Description

Function that returns the specified BRepCoEdgeDefinition object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCoEdgeDefinitions\_var" is a variable referencing a [BRepCoEdgeDefinitions](BRepCoEdgeDefinitions.htm) object.```` ``` returnValue = bRepCoEdgeDefinitions_var.item(index) ``` ```` |

"bRepCoEdgeDefinitions\_var" is a variable referencing a [BRepCoEdgeDefinitions](BRepCoEdgeDefinitions.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepCoEdgeDefinition](BRepCoEdgeDefinition.htm) | Returns the specified item or null if an invalid index was specified. |

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