# BRepBodies.item Method

Parent Object: [BRepBodies](BRepBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBodies.h>

## Description

Function that returns the specified body using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBodies\_var" is a variable referencing a [BRepBodies](BRepBodies.htm) object.```` ``` returnValue = bRepBodies_var.item(index) ``` ```` |

"bRepBodies\_var" is a variable referencing a [BRepBodies](BRepBodies.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepBody](BRepBody.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Get Volume of Active Design API Sample](GetsVolumeOfActiveDesign_Sample.htm) | Traverses through the active design and totals the volume of every body within the design. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |