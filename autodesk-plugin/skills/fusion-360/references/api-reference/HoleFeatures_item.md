# HoleFeatures.item Method

Parent Object: [HoleFeatures](HoleFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeatures.h>

## Description

Function that returns the specified hole feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeatures\_var" is a variable referencing a [HoleFeatures](HoleFeatures.htm) object.```` ``` returnValue = holeFeatures_var.item(index) ``` ```` |

"holeFeatures\_var" is a variable referencing a [HoleFeatures](HoleFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [HoleFeature](HoleFeature.htm) | Returns the specified item or null if an invalid index was specified. |

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