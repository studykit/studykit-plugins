# Occurrence.getPhysicalProperties Method

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

Returns the PhysicalProperties object that has properties for getting the area, density, mass, volume, moments, etc of this occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an [Occurrence](Occurrence.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"occurrence\_var" is a variable referencing an [Occurrence](Occurrence.htm) object.  ```` ``` #include <Fusion/Components/Occurrence.h>  // Uses no optional arguments. returnValue = occurrence_var->getPhysicalProperties();  // Uses optional arguments. returnValue = occurrence_var->getPhysicalProperties(accuracy); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PhysicalProperties](PhysicalProperties.htm) | Returns a PhysicalProperties object that can be used to get the various physical property related values. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| accuracy | [CalculationAccuracy](CalculationAccuracy.htm) | Specifies the desired level of computational accuracy of the property calculations. The default value of 'LowCalculationAccuracy' returns results within a +/- 1% error margin.   This is an optional argument whose default value is CalculationAccuracy.LowCalculationAccuracy. |

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