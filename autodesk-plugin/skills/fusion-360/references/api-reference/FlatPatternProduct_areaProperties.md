# FlatPatternProduct.areaProperties Method

Parent Object: [FlatPatternProduct](FlatPatternProduct.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternProduct.h>

## Description

Returns the AreaProperties object that has properties for getting the area, perimeter, centroid, etc for a collection of 2D sketch profiles and/or planar surfaces that all lie on the same plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternProduct\_var" is a variable referencing a [FlatPatternProduct](FlatPatternProduct.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"flatPatternProduct\_var" is a variable referencing a [FlatPatternProduct](FlatPatternProduct.htm) object.  ```` ``` #include <Fusion/SheetMetal/FlatPatternProduct.h>  // Uses no optional arguments. returnValue = flatPatternProduct_var->areaProperties(inputs);  // Uses optional arguments. returnValue = flatPatternProduct_var->areaProperties(inputs, accuracy); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [AreaProperties](AreaProperties.htm) | Returns an AreaProperties object that can be used to examine the area results. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputs | [ObjectCollection](ObjectCollection.htm) | A collection of one or more 2D sketch profile and/or planar surface input objects to perform the calculations on. Supported input object types are 2D closed sketch profiles and planar surfaces. Object must all lie on the same plane. Calculation results reflect the sums of the input objects (i.e. total area of multiple sketch profiles) |
| accuracy | [CalculationAccuracy](CalculationAccuracy.htm) | Specifies the desired level of computational accuracy of the property calculations. The default value of 'LowCalculationAccuracy' returns results within a +/- 1% error margin.   This is an optional argument whose default value is CalculationAccuracy.LowCalculationAccuracy. |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |