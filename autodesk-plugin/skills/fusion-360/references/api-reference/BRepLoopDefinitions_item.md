# BRepLoopDefinitions.item Method

Parent Object: [BRepLoopDefinitions](BRepLoopDefinitions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoopDefinitions.h>

## Description

Function that returns the specified BRepLoopDefinition object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLoopDefinitions\_var" is a variable referencing a [BRepLoopDefinitions](BRepLoopDefinitions.htm) object.```` ``` returnValue = bRepLoopDefinitions_var.item(index) ``` ```` |

"bRepLoopDefinitions\_var" is a variable referencing a [BRepLoopDefinitions](BRepLoopDefinitions.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepLoopDefinition](BRepLoopDefinition.htm) | Returns the specified item or null if an invalid index was specified. |

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