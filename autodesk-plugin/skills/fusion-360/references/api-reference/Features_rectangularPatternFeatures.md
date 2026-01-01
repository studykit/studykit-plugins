# Features.rectangularPatternFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the rectangular pattern features within the component and supports the creation of new rectangular pattern features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<RectangularPatternFeatures> propertyValue = features_var->rectangularPatternFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [RectangularPatternFeatures](RectangularPatternFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Manage Participant Bodies API Sample](ParticipantBodiesSample_Sample.htm) | Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also. |
| [rectangularPattern.add](rectangularPatter_add_Sample.htm) | Demonstrates the rectangularPattern.add method using a selected body and two selected edges to define the directions. |
| [RectangularPattern Feature](RectangularPatternFeatureSample_Sample.htm) | Demonstrates creating a new rectangular pattern feature. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |