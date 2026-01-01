# PathPatternFeatures.item Method

Parent Object: [PathPatternFeatures](PathPatternFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeatures.h>

## Description

Function that returns the specified path pattern feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeatures\_var" is a variable referencing a [PathPatternFeatures](PathPatternFeatures.htm) object.```` ``` returnValue = pathPatternFeatures_var.item(index) ``` ```` |

"pathPatternFeatures\_var" is a variable referencing a [PathPatternFeatures](PathPatternFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PathPatternFeature](PathPatternFeature.htm) | Returns the specified item or null if an invalid index was specified. |

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