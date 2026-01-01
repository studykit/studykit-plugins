# LoftFeatures.item Method

Parent Object: [LoftFeatures](LoftFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeatures.h>

## Description

Function that returns the specified loft feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeatures\_var" is a variable referencing a [LoftFeatures](LoftFeatures.htm) object.```` ``` returnValue = loftFeatures_var.item(index) ``` ```` |

"loftFeatures\_var" is a variable referencing a [LoftFeatures](LoftFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [LoftFeature](LoftFeature.htm) | Returns the specified item or null if an invalid index was specified. |

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