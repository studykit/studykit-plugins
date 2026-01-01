# SweepFeatureInput.distanceOne Property

Parent Object: [SweepFeatureInput](SweepFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatureInput.h>

## Description

Gets and sets the distance for the first side. The distance is a value from 0 to 1 indicating the position along the path where 0 is at the start and 1 is at the end. The value is default to 1.0.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. |

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. ```` ``` #include <Fusion/Features/SweepFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = sweepFeatureInput_var->distanceOne();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = sweepFeatureInput_var->distanceOne(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |