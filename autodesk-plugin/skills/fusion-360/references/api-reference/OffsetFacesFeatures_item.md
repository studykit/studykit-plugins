# OffsetFacesFeatures.item Method

Parent Object: [OffsetFacesFeatures](OffsetFacesFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFacesFeatures.h>

## Description

Function that returns the specified Offset Face feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFacesFeatures\_var" is a variable referencing an [OffsetFacesFeatures](OffsetFacesFeatures.htm) object.```` ``` returnValue = offsetFacesFeatures_var.item(index) ``` ```` |

"offsetFacesFeatures\_var" is a variable referencing an [OffsetFacesFeatures](OffsetFacesFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [OffsetFacesFeature](OffsetFacesFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |