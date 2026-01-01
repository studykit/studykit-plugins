# Design.physicalProperties Method

Parent Object: [Design](Design.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

Returns the PhysicalProperties object that has properties for getting the area, density, mass, volume, moments, etc for a collection of 3D solid objects.

## Syntax

* [Python](#Python)
* [C++](#C++)

"design\_var" is a variable referencing a [Design](Design.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"design\_var" is a variable referencing a [Design](Design.htm) object.  ```` ``` #include <Fusion/Fusion/Design.h>  // Uses no optional arguments. returnValue = design_var->physicalProperties(inputs);  // Uses optional arguments. returnValue = design_var->physicalProperties(inputs, accuracy); ``` ```` |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputs | [ObjectCollection](ObjectCollection.htm) | A collection of one or more 3D solid input objects to perform the calculations on. Supported input object types are Components, Occurrences and BRepBodies. Calculation results reflect the sums of the input objects (i.e. total volume of multiple bodies) |
| accuracy | [CalculationAccuracy](CalculationAccuracy.htm) | Specifies the desired level of computational accuracy of the property calculations. The default value of 'LowCalculationAccuracy' returns results within a +/- 1% error margin.   This is an optional argument whose default value is CalculationAccuracy.LowCalculationAccuracy. |

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |