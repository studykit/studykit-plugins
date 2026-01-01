# RevolveFeatureInput.isSolid Property

Parent Object: [RevolveFeatureInput](RevolveFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeatureInput.h>

## Description

Specifies if the revolution should be created as a solid or surface. If it's a surface then there aren't any end caps and it's open. This is initialized to true so a solid will be created if it's not changed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeatureInput\_var" is a variable referencing a RevolveFeatureInput object. |

"revolveFeatureInput\_var" is a variable referencing a RevolveFeatureInput object. ```` ``` #include <Fusion/Features/RevolveFeatureInput.h>  // Get the value of the property. boolean propertyValue = revolveFeatureInput_var->isSolid();  // Set the value of the property, where value_var is a boolean. bool returnValue = revolveFeatureInput_var->isSolid(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |