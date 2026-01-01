# BoundaryFillFeatures.item Method

Parent Object: [BoundaryFillFeatures](BoundaryFillFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeatures.h>

## Description

Function that returns the specified boundary fill feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeatures\_var" is a variable referencing a [BoundaryFillFeatures](BoundaryFillFeatures.htm) object.```` ``` returnValue = boundaryFillFeatures_var.item(index) ``` ```` |

"boundaryFillFeatures\_var" is a variable referencing a [BoundaryFillFeatures](BoundaryFillFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BoundaryFillFeature](BoundaryFillFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |