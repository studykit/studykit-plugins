# SweepFeature.guideRail Property

Parent Object: [SweepFeature](SweepFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeature.h>

## Description

Gets and sets the guide rail to create the sweep. This can be set to null to have a path only sweep.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeature\_var" is a variable referencing a SweepFeature object.  ```` ``` # Get the value of the property. propertyValue = sweepFeature_var.guideRail  # Set the value of the property. sweepFeature_var.guideRail = propertyValue ``` ```` |

"sweepFeature\_var" is a variable referencing a SweepFeature object. ```` ``` #include <Fusion/Features/SweepFeature.h>  // Get the value of the property. Ptr<Path> propertyValue = sweepFeature_var->guideRail();  // Set the value of the property, where value_var is a Path. bool returnValue = sweepFeature_var->guideRail(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Path](Path.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |