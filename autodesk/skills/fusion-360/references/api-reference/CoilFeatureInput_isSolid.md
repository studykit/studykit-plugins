# CoilFeatureInput.isSolid Property

Parent Object: [CoilFeatureInput](CoilFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CoilFeatureInput.h>

## Description

Specifies if the coil should be created as a solid or surface. This is initialized to true so a solid will be created if it's not changed. It only can be set to false in non-parametric modeling.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coilFeatureInput\_var" is a variable referencing a CoilFeatureInput object. |

"coilFeatureInput\_var" is a variable referencing a CoilFeatureInput object. ```` ``` #include <Fusion/Features/CoilFeatureInput.h>  // Get the value of the property. boolean propertyValue = coilFeatureInput_var->isSolid();  // Set the value of the property, where value_var is a boolean. bool returnValue = coilFeatureInput_var->isSolid(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |