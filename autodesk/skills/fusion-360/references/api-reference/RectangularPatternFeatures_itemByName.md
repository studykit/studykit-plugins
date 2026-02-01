# RectangularPatternFeatures.itemByName Method

Parent Object: [RectangularPatternFeatures](RectangularPatternFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RectangularPatternFeatures.h>

## Description

Function that returns the specified rectangular pattern feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternFeatures\_var" is a variable referencing a [RectangularPatternFeatures](RectangularPatternFeatures.htm) object.```` ``` returnValue = rectangularPatternFeatures_var.itemByName(name) ``` ```` |

"rectangularPatternFeatures\_var" is a variable referencing a [RectangularPatternFeatures](RectangularPatternFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RectangularPatternFeature](RectangularPatternFeature.htm) | Returns the specified item or null if the specified name was not found. |

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