# PatchFeatures.item Method

Parent Object: [PatchFeatures](PatchFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeatures.h>

## Description

Function that returns the specified patch feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeatures\_var" is a variable referencing a [PatchFeatures](PatchFeatures.htm) object.```` ``` returnValue = patchFeatures_var.item(index) ``` ```` |

"patchFeatures\_var" is a variable referencing a [PatchFeatures](PatchFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PatchFeature](PatchFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |