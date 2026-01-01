# SweepFeatureInput.extent Property

Parent Object: [SweepFeatureInput](SweepFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatureInput.h>

## Description

Gets and sets the sweep extent type. It defaults to PerpendicularToPathExtentType. This property is ignored when a guide rail has not been specified.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. |

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. ```` ``` #include <Fusion/Features/SweepFeatureInput.h>  // Get the value of the property. SweepExtentTypes propertyValue = sweepFeatureInput_var->extent();  // Set the value of the property, where value_var is a SweepExtentTypes. bool returnValue = sweepFeatureInput_var->extent(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SweepExtentTypes](SweepExtentTypes.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |