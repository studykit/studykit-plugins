# Features.pathPatternFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the path pattern features within the component and supports the creation of new path pattern features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<PathPatternFeatures> propertyValue = features_var->pathPatternFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [PathPatternFeatures](PathPatternFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [pathPatternFeatures.add](pathPatternFeatures_add_Sample.htm) | Demonstrates the pathPatternFeatures.add method using a selected body and sketch curve as the path. |
| [Path Pattern Feature API Sample](PathPatternFeatureSample_Sample.htm) | Demonstrates creating a new path pattern feature. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |