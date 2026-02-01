# SweepFeatureInput.solidOrientation Property

Parent Object: [SweepFeatureInput](SweepFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatureInput.h>

## Description

Gets and sets the solid sweep orientation. It defaults to PerpendicularSolidOrientationType. Setting the solid orientation to AlignedSolidOrientationType requires the solid aligned axis to be set. This property is ignored if sweeping a profile.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. |

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. ```` ``` #include <Fusion/Features/SweepFeatureInput.h>  // Get the value of the property. SweepSolidOrientationTypes propertyValue = sweepFeatureInput_var->solidOrientation();  // Set the value of the property, where value_var is a SweepSolidOrientationTypes. bool returnValue = sweepFeatureInput_var->solidOrientation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SweepSolidOrientationTypes](SweepSolidOrientationTypes.htm).

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |