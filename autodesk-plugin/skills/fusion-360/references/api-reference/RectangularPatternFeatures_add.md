# RectangularPatternFeatures.add Method

Parent Object: [RectangularPatternFeatures](RectangularPatternFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RectangularPatternFeatures.h>

## Description

Creates a new rectangular pattern feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternFeatures\_var" is a variable referencing a [RectangularPatternFeatures](RectangularPatternFeatures.htm) object.```` ``` returnValue = rectangularPatternFeatures_var.add(input) ``` ```` |

"rectangularPatternFeatures\_var" is a variable referencing a [RectangularPatternFeatures](RectangularPatternFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RectangularPatternFeature](RectangularPatternFeature.htm) | Returns the newly created RectangularPatternFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [RectangularPatternFeatureInput](RectangularPatternFeatureInput.htm) | A RectangularPatternFeatureInput object that defines the desired rectangular pattern. Use the createInput method to create a new RectangularPatternFeatureInput object and then use methods on it (the RectangularPatternFeatureInput object) to define the rectangular pattern. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Manage Participant Bodies API Sample](ParticipantBodiesSample_Sample.htm) | Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also. |
| [rectangularPattern.add](rectangularPatter_add_Sample.htm) | Demonstrates the rectangularPattern.add method using a selected body and two selected edges to define the directions. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |