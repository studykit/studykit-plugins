# ExtendFeatures.item Method

Parent Object: [ExtendFeatures](ExtendFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeatures.h>

## Description

Function that returns the specified extend feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeatures\_var" is a variable referencing an [ExtendFeatures](ExtendFeatures.htm) object.```` ``` returnValue = extendFeatures_var.item(index) ``` ```` |

"extendFeatures\_var" is a variable referencing an [ExtendFeatures](ExtendFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ExtendFeature](ExtendFeature.htm) | Returns the specified item or null if an invalid index was specified. |

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