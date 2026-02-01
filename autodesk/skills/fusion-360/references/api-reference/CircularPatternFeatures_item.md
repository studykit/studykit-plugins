# CircularPatternFeatures.item Method

Parent Object: [CircularPatternFeatures](CircularPatternFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeatures.h>

## Description

Function that returns the specified circular pattern feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternFeatures\_var" is a variable referencing a [CircularPatternFeatures](CircularPatternFeatures.htm) object.```` ``` returnValue = circularPatternFeatures_var.item(index) ``` ```` |

"circularPatternFeatures\_var" is a variable referencing a [CircularPatternFeatures](CircularPatternFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CircularPatternFeature](CircularPatternFeature.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |