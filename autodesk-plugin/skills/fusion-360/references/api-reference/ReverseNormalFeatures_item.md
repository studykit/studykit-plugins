# ReverseNormalFeatures.item Method

Parent Object: [ReverseNormalFeatures](ReverseNormalFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReverseNormalFeatures.h>

## Description

Function that returns the specified Reverse Normal feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"reverseNormalFeatures\_var" is a variable referencing a [ReverseNormalFeatures](ReverseNormalFeatures.htm) object.```` ``` returnValue = reverseNormalFeatures_var.item(index) ``` ```` |

"reverseNormalFeatures\_var" is a variable referencing a [ReverseNormalFeatures](ReverseNormalFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ReverseNormalFeature](ReverseNormalFeature.htm) | Returns the specified item or null if an invalid index was specified. |

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