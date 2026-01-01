# BRepBody.getPhysicalProperties Method

Parent Object: [BRepBody](BRepBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBody.h>

## Description

Returns the PhysicalProperties object that has properties for getting the area, density, mass, volume, moments, etc of this body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBody\_var" is a variable referencing a [BRepBody](BRepBody.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"bRepBody\_var" is a variable referencing a [BRepBody](BRepBody.htm) object.  ```` ``` #include <Fusion/BRep/BRepBody.h>  // Uses no optional arguments. returnValue = bRepBody_var->getPhysicalProperties();  // Uses optional arguments. returnValue = bRepBody_var->getPhysicalProperties(accuracy); ``` ```` |

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

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |