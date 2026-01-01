# SweepFeatureInput.isSolid Property

Parent Object: [SweepFeatureInput](SweepFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatureInput.h>

## Description

Specifies if the sweep should be created as a solid or surface. If it's a surface then there aren't any end caps and it's open. This is initialized to true so a solid will be created if it's not changed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. |

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. ```` ``` #include <Fusion/Features/SweepFeatureInput.h>  // Get the value of the property. boolean propertyValue = sweepFeatureInput_var->isSolid();  // Set the value of the property, where value_var is a boolean. bool returnValue = sweepFeatureInput_var->isSolid(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |