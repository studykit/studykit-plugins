# MeasureResults.value Property

Parent Object: [MeasureResults](MeasureResults.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MeasureResults.h>

## Description

The measurement value. If the measurement is a distance this value will be in centimeters. If it's an angle then it will be in radians.

## Syntax

* [Python](#Python)
* [C++](#C++)

"measureResults\_var" is a variable referencing a MeasureResults object. |

"measureResults\_var" is a variable referencing a MeasureResults object. ```` ``` #include <Core/Application/MeasureResults.h>  // Get the value of the property. double propertyValue = measureResults_var->value(); ``` ```` |

## Property Value

This is a read only property whose value is a double.

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