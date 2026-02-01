# AreaProperties.accuracy Property

Parent Object: [AreaProperties](AreaProperties.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/AreaProperties.h>

## Description

Returns the accuracy that was used for the calculation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"areaProperties\_var" is a variable referencing an AreaProperties object. |

"areaProperties\_var" is a variable referencing an AreaProperties object. ```` ``` #include <Fusion/Fusion/AreaProperties.h>  // Get the value of the property. CalculationAccuracy propertyValue = areaProperties_var->accuracy(); ``` ```` |

## Property Value

This is a read only property whose value is a [CalculationAccuracy](CalculationAccuracy.htm).

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