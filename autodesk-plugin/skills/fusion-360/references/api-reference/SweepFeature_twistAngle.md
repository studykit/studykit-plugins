# SweepFeature.twistAngle Property

Parent Object: [SweepFeature](SweepFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeature.h>

## Description

Gets the ModelParameter that defines the twist angle of the sweep feature. The value of the angle can be edited by using the properties on the ModelParameter object to edit the parameter. When sweeping a solid setting the twist angle requires the solid twist axis to be set. This property is ignored if a guide rail or surface has been specified.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeature\_var" is a variable referencing a SweepFeature object. |

"sweepFeature\_var" is a variable referencing a SweepFeature object. ```` ``` #include <Fusion/Features/SweepFeature.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = sweepFeature_var->twistAngle(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |