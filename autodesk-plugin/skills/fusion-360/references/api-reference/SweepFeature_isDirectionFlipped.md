# SweepFeature.isDirectionFlipped Property

Parent Object: [SweepFeature](SweepFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeature.h>

## Description

Gets and sets if the direction of the sweep is flipped. This property only applies to sweep features that include a guide rail and whose path runs on both sides of the profile.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeature\_var" is a variable referencing a SweepFeature object.  ```` ``` # Get the value of the property. propertyValue = sweepFeature_var.isDirectionFlipped  # Set the value of the property. sweepFeature_var.isDirectionFlipped = propertyValue ``` ```` |

"sweepFeature\_var" is a variable referencing a SweepFeature object. ```` ``` #include <Fusion/Features/SweepFeature.h>  // Get the value of the property. boolean propertyValue = sweepFeature_var->isDirectionFlipped();  // Set the value of the property, where value_var is a boolean. bool returnValue = sweepFeature_var->isDirectionFlipped(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |