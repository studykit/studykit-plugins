# PathPatternFeatures.itemByName Method

Parent Object: [PathPatternFeatures](PathPatternFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeatures.h>

## Description

Function that returns the specified path pattern feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeatures\_var" is a variable referencing a [PathPatternFeatures](PathPatternFeatures.htm) object.```` ``` returnValue = pathPatternFeatures_var.itemByName(name) ``` ```` |

"pathPatternFeatures\_var" is a variable referencing a [PathPatternFeatures](PathPatternFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PathPatternFeature](PathPatternFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |