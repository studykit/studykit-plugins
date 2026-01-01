# PathPatternFeatures.add Method

Parent Object: [PathPatternFeatures](PathPatternFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeatures.h>

## Description

Creates a new path pattern feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeatures\_var" is a variable referencing a [PathPatternFeatures](PathPatternFeatures.htm) object.```` ``` returnValue = pathPatternFeatures_var.add(input) ``` ```` |

"pathPatternFeatures\_var" is a variable referencing a [PathPatternFeatures](PathPatternFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PathPatternFeature](PathPatternFeature.htm) | Returns the newly created PathPatternFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [PathPatternFeatureInput](PathPatternFeatureInput.htm) | A PathPatternFeatureInput object that defines the desired path pattern. Use the createInput method to create a new PathPatternFeatureInput object and then use methods on it (the PathPatternFeatureInput object) to define the path pattern. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [pathPatternFeatures.add](pathPatternFeatures_add_Sample.htm) | Demonstrates the pathPatternFeatures.add method using a selected body and sketch curve as the path. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |