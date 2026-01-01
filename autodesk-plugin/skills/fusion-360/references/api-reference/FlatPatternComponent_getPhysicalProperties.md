# FlatPatternComponent.getPhysicalProperties Method

Parent Object: [FlatPatternComponent](FlatPatternComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

Returns the PhysicalProperties object that has properties for getting the area, density, mass, volume, moments, etc of this component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternComponent\_var" is a variable referencing a [FlatPatternComponent](FlatPatternComponent.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"flatPatternComponent\_var" is a variable referencing a [FlatPatternComponent](FlatPatternComponent.htm) object.  ```` ``` #include <Fusion/SheetMetal/FlatPatternComponent.h>  // Uses no optional arguments. returnValue = flatPatternComponent_var->getPhysicalProperties();  // Uses optional arguments. returnValue = flatPatternComponent_var->getPhysicalProperties(accuracy); ``` ```` |

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

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |