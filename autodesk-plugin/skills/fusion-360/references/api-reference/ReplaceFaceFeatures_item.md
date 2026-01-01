# ReplaceFaceFeatures.item Method

Parent Object: [ReplaceFaceFeatures](ReplaceFaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReplaceFaceFeatures.h>

## Description

Function that returns the specified replace face feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"replaceFaceFeatures\_var" is a variable referencing a [ReplaceFaceFeatures](ReplaceFaceFeatures.htm) object.```` ``` returnValue = replaceFaceFeatures_var.item(index) ``` ```` |

"replaceFaceFeatures\_var" is a variable referencing a [ReplaceFaceFeatures](ReplaceFaceFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ReplaceFaceFeature](ReplaceFaceFeature.htm) | Returns the specified item or null if an invalid index was specified. |

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