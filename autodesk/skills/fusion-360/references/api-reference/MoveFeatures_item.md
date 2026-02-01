# MoveFeatures.item Method

Parent Object: [MoveFeatures](MoveFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatures.h>

## Description

Function that returns the specified move feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatures\_var" is a variable referencing a [MoveFeatures](MoveFeatures.htm) object.```` ``` returnValue = moveFeatures_var.item(index) ``` ```` |

"moveFeatures\_var" is a variable referencing a [MoveFeatures](MoveFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MoveFeature](MoveFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |