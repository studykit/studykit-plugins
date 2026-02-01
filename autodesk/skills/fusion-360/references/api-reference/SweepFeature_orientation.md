# SweepFeature.orientation Property

Parent Object: [SweepFeature](SweepFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeature.h>

## Description

Gets and sets the sweep orientation. It defaults to PerpendicularOrientationType. This property is ignored if sweeping a solid or a guide rail or surface has been specified.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeature\_var" is a variable referencing a SweepFeature object.  ```` ``` # Get the value of the property. propertyValue = sweepFeature_var.orientation  # Set the value of the property. sweepFeature_var.orientation = propertyValue ``` ```` |

"sweepFeature\_var" is a variable referencing a SweepFeature object. ```` ``` #include <Fusion/Features/SweepFeature.h>  // Get the value of the property. SweepOrientationTypes propertyValue = sweepFeature_var->orientation();  // Set the value of the property, where value_var is a SweepOrientationTypes. bool returnValue = sweepFeature_var->orientation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SweepOrientationTypes](SweepOrientationTypes.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |