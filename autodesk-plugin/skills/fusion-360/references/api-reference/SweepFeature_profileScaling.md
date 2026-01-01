# SweepFeature.profileScaling Property

Parent Object: [SweepFeature](SweepFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeature.h>

## Description

Gets and sets the sweep profile scaling option. It defaults to SweepProfileScaleOption. This property is only used when a guide rail has been specified.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeature\_var" is a variable referencing a SweepFeature object.  ```` ``` # Get the value of the property. propertyValue = sweepFeature_var.profileScaling  # Set the value of the property. sweepFeature_var.profileScaling = propertyValue ``` ```` |

"sweepFeature\_var" is a variable referencing a SweepFeature object. ```` ``` #include <Fusion/Features/SweepFeature.h>  // Get the value of the property. SweepProfileScalingOptions propertyValue = sweepFeature_var->profileScaling();  // Set the value of the property, where value_var is a SweepProfileScalingOptions. bool returnValue = sweepFeature_var->profileScaling(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SweepProfileScalingOptions](SweepProfileScalingOptions.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |