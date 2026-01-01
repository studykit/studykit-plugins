# SweepFeature.solidOrientation Property

Parent Object: [SweepFeature](SweepFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeature.h>

## Description

Gets and sets the sweep solid orientation. It defaults to PerpendicularSolidOrientationType. Setting the solid orientation to AlignedSolidOrientationType requires the solid aligned axis to be set. This property is ignored if sweeping a profile.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeature\_var" is a variable referencing a SweepFeature object.  ```` ``` # Get the value of the property. propertyValue = sweepFeature_var.solidOrientation  # Set the value of the property. sweepFeature_var.solidOrientation = propertyValue ``` ```` |

"sweepFeature\_var" is a variable referencing a SweepFeature object. ```` ``` #include <Fusion/Features/SweepFeature.h>  // Get the value of the property. SweepSolidOrientationTypes propertyValue = sweepFeature_var->solidOrientation();  // Set the value of the property, where value_var is a SweepSolidOrientationTypes. bool returnValue = sweepFeature_var->solidOrientation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SweepSolidOrientationTypes](SweepSolidOrientationTypes.htm).

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |