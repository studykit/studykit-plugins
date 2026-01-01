# ArrangeFeatures.item Method

Parent Object: [ArrangeFeatures](ArrangeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeatures.h>

## Description

Returns the specified Arrange feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeatures\_var" is a variable referencing an [ArrangeFeatures](ArrangeFeatures.htm) object.```` ``` returnValue = arrangeFeatures_var.item(index) ``` ```` |

"arrangeFeatures\_var" is a variable referencing an [ArrangeFeatures](ArrangeFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ArrangeFeature](ArrangeFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |