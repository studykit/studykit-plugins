# MeasureResults.positionOne Property

Parent Object: [MeasureResults](MeasureResults.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MeasureResults.h>

## Description

For a distance measurement, this is the point on the first entity where the measurement was made from. For an angle measurement this is one of the three points defining the angle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"measureResults\_var" is a variable referencing a MeasureResults object. |

"measureResults\_var" is a variable referencing a MeasureResults object. ```` ``` #include <Core/Application/MeasureResults.h>  // Get the value of the property. Ptr<Point3D> propertyValue = measureResults_var->positionOne(); ``` ```` |

## Property Value

This is a read only property whose value is a [Point3D](Point3D.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Measure Sample](MeasureSample_Sample.htm) | Measure related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |