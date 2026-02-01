# ScaleFeatures.item Method

Parent Object: [ScaleFeatures](ScaleFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeatures.h>

## Description

Function that returns the specified scale feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeatures\_var" is a variable referencing a [ScaleFeatures](ScaleFeatures.htm) object.```` ``` returnValue = scaleFeatures_var.item(index) ``` ```` |

"scaleFeatures\_var" is a variable referencing a [ScaleFeatures](ScaleFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ScaleFeature](ScaleFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |