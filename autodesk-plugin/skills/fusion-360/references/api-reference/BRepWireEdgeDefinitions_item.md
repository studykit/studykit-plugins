# BRepWireEdgeDefinitions.item Method

Parent Object: [BRepWireEdgeDefinitions](BRepWireEdgeDefinitions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWireEdgeDefinitions.h>

## Description

Function that returns the specified BRepWireEdgeDefinition object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWireEdgeDefinitions\_var" is a variable referencing a [BRepWireEdgeDefinitions](BRepWireEdgeDefinitions.htm) object.```` ``` returnValue = bRepWireEdgeDefinitions_var.item(index) ``` ```` |

"bRepWireEdgeDefinitions\_var" is a variable referencing a [BRepWireEdgeDefinitions](BRepWireEdgeDefinitions.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepWireEdgeDefinition](BRepWireEdgeDefinition.htm) | Returns the specified item or null if an invalid index was specified. |

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