# AreaProperties.perimeter Property

Parent Object: [AreaProperties](AreaProperties.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/AreaProperties.h>

## Description

Gets the perimeter in centimeters. The perimeter is the sum of the length of all the curves or edges of the profile or planar surface

## Syntax

* [Python](#Python)
* [C++](#C++)

"areaProperties\_var" is a variable referencing an AreaProperties object. |

"areaProperties\_var" is a variable referencing an AreaProperties object. ```` ``` #include <Fusion/Fusion/AreaProperties.h>  // Get the value of the property. double propertyValue = areaProperties_var->perimeter(); ``` ```` |

## Property Value

This is a read only property whose value is a double.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample for AreaProperties](AreaPropertiesSample_Sample.htm) | Demonstrates how to use AreaProperties |

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |