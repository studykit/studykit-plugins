# CoilFeatureInput.isClockwiseRotation Property

Parent Object: [CoilFeatureInput](CoilFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CoilFeatureInput.h>

## Description

Gets and sets whether the rotation is clockwise or counter-clockwise. A value of true indicates clockwise rotation. It defaults to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coilFeatureInput\_var" is a variable referencing a CoilFeatureInput object. |

"coilFeatureInput\_var" is a variable referencing a CoilFeatureInput object. ```` ``` #include <Fusion/Features/CoilFeatureInput.h>  // Get the value of the property. boolean propertyValue = coilFeatureInput_var->isClockwiseRotation();  // Set the value of the property, where value_var is a boolean. bool returnValue = coilFeatureInput_var->isClockwiseRotation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |