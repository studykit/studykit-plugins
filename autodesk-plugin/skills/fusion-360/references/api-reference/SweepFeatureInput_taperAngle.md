# SweepFeatureInput.taperAngle Property

Parent Object: [SweepFeatureInput](SweepFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatureInput.h>

## Description

Gets and sets the taper angle of the sweep. This property is initialized with a taper angle of zero. A negative angle will taper the sweep inward while a positive value will taper the sweep outward.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = sweepFeatureInput_var.taperAngle  # Set the value of the property. sweepFeatureInput_var.taperAngle = propertyValue ``` ```` |

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. ```` ``` #include <Fusion/Features/SweepFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = sweepFeatureInput_var->taperAngle();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = sweepFeatureInput_var->taperAngle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |