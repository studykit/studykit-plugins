# SplitFaceFeatures.item Method

Parent Object: [SplitFaceFeatures](SplitFaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeatures.h>

## Description

Function that returns the specified split face feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitFaceFeatures\_var" is a variable referencing a [SplitFaceFeatures](SplitFaceFeatures.htm) object.```` ``` returnValue = splitFaceFeatures_var.item(index) ``` ```` |

"splitFaceFeatures\_var" is a variable referencing a [SplitFaceFeatures](SplitFaceFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SplitFaceFeature](SplitFaceFeature.htm) | Returns the specified item or null if an invalid index was specified. |

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