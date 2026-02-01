# SweepFeature.extent Property

Parent Object: [SweepFeature](SweepFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeature.h>

## Description

Gets and sets the sweep extent type. It defaults to PerpendicularToPathExtentType. When sweeping a solid setting the twist angle requires the solid twist axis to be set. This property is ignored when a guide rail has not been specified.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeature\_var" is a variable referencing a SweepFeature object. |

"sweepFeature\_var" is a variable referencing a SweepFeature object. ```` ``` #include <Fusion/Features/SweepFeature.h>  // Get the value of the property. SweepExtentTypes propertyValue = sweepFeature_var->extent();  // Set the value of the property, where value_var is a SweepExtentTypes. bool returnValue = sweepFeature_var->extent(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SweepExtentTypes](SweepExtentTypes.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |