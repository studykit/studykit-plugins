# SweepFeatureInput.twistAngle Property

Parent Object: [SweepFeatureInput](SweepFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatureInput.h>

## Description

Gets and sets the twist angle of the sweep. This property is initialized with a twist angle of zero. When sweeping a solid setting the twist angle requires the solid twist axis to be set.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = sweepFeatureInput_var.twistAngle  # Set the value of the property. sweepFeatureInput_var.twistAngle = propertyValue ``` ```` |

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. ```` ``` #include <Fusion/Features/SweepFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = sweepFeatureInput_var->twistAngle();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = sweepFeatureInput_var->twistAngle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |