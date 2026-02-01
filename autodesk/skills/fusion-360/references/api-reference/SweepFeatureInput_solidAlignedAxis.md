# SweepFeatureInput.solidAlignedAxis Property

Parent Object: [SweepFeatureInput](SweepFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatureInput.h>

## Description

Gets and sets the axis to align the solid being swept with. The axis is used when sweeping a solid, and the solid orientation is set to AlignedSolidOrientationType. It can be a sketch line, linear edge, or construction axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. |

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. ```` ``` #include <Fusion/Features/SweepFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = sweepFeatureInput_var->solidAlignedAxis();  // Set the value of the property, where value_var is a Base. bool returnValue = sweepFeatureInput_var->solidAlignedAxis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |