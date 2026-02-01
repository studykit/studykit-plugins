# DeleteFaceFeatures.item Method

Parent Object: [DeleteFaceFeatures](DeleteFaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DeleteFaceFeatures.h>

## Description

Function that returns the specified DeleteFaceFeature object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"deleteFaceFeatures\_var" is a variable referencing a [DeleteFaceFeatures](DeleteFaceFeatures.htm) object.```` ``` returnValue = deleteFaceFeatures_var.item(index) ``` ```` |

"deleteFaceFeatures\_var" is a variable referencing a [DeleteFaceFeatures](DeleteFaceFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DeleteFaceFeature](DeleteFaceFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |