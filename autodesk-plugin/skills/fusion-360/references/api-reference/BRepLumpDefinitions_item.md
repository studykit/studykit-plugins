# BRepLumpDefinitions.item Method

Parent Object: [BRepLumpDefinitions](BRepLumpDefinitions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLumpDefinitions.h>

## Description

Function that returns the specified BRepLumpDefinition object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLumpDefinitions\_var" is a variable referencing a [BRepLumpDefinitions](BRepLumpDefinitions.htm) object.```` ``` returnValue = bRepLumpDefinitions_var.item(index) ``` ```` |

"bRepLumpDefinitions\_var" is a variable referencing a [BRepLumpDefinitions](BRepLumpDefinitions.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepLumpDefinition](BRepLumpDefinition.htm) | Returns the specified item or null if an invalid index was specified. |

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