# SweepFeatureInput.distanceTwo Property

Parent Object: [SweepFeatureInput](SweepFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatureInput.h>

## Description

Gets and sets the distance for the second side. The distance is a value from 0 to 1 indicating the position along the path where 0 is at the start and 1 is at the end. The value defaults to 0 in the case where the path is closed, otherwise it defaults to 1.0. It is ignored if the path is only on one side of the profile or if the sweep definition includes a guide rail. It's always the distance against the normal of the profile if available.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. |

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. ```` ``` #include <Fusion/Features/SweepFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = sweepFeatureInput_var->distanceTwo();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = sweepFeatureInput_var->distanceTwo(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |