# PhysicalProperties.accuracy Property

Parent Object: [PhysicalProperties](PhysicalProperties.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/PhysicalProperties.h>

## Description

Returns the accuracy that was used for the calculation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"physicalProperties\_var" is a variable referencing a PhysicalProperties object. |

"physicalProperties\_var" is a variable referencing a PhysicalProperties object. ```` ``` #include <Fusion/Fusion/PhysicalProperties.h>  // Get the value of the property. CalculationAccuracy propertyValue = physicalProperties_var->accuracy(); ``` ```` |

## Property Value

This is a read only property whose value is a [CalculationAccuracy](CalculationAccuracy.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Get Physical Properties API Sample](GetPhysicalProperties_Sample.htm) | Script that demonstrates getting physical properties using the API. When this script is run it will create a new document, build a simple model, and get the various physical properties from the model. |

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |