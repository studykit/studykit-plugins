# CircularPatternFeatures.itemByName Method

Parent Object: [CircularPatternFeatures](CircularPatternFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeatures.h>

## Description

Function that returns the specified circular pattern feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternFeatures\_var" is a variable referencing a [CircularPatternFeatures](CircularPatternFeatures.htm) object.```` ``` returnValue = circularPatternFeatures_var.itemByName(name) ``` ```` |

"circularPatternFeatures\_var" is a variable referencing a [CircularPatternFeatures](CircularPatternFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CircularPatternFeature](CircularPatternFeature.htm) | Returns the specified item or null if the specified name was not found. |

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