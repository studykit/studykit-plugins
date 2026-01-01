# Profile.areaProperties Method

Parent Object: [Profile](Profile.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Profile.h>

## Description

Calculates the area properties for the profile.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profile\_var" is a variable referencing a [Profile](Profile.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"profile\_var" is a variable referencing a [Profile](Profile.htm) object.  ```` ``` #include <Fusion/Sketch/Profile.h>  // Uses no optional arguments. returnValue = profile_var->areaProperties();  // Uses optional arguments. returnValue = profile_var->areaProperties(accuracy); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [AreaProperties](AreaProperties.htm) | Returns the AreaProperties object that has properties for getting the area, perimeter, centroid, etc of this profile. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| accuracy | [CalculationAccuracy](CalculationAccuracy.htm) | Specifies the desired level of computational accuracy of the property calculations. The default value of 'LowCalculationAccuracy' returns results within a +/- 1% error margin.   This is an optional argument whose default value is CalculationAccuracy.LowCalculationAccuracy. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample for AreaProperties](AreaPropertiesSample_Sample.htm) | Demonstrates how to use AreaProperties |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |