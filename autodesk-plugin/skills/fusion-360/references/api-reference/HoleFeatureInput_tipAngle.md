# HoleFeatureInput.tipAngle Property

Parent Object: [HoleFeatureInput](HoleFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeatureInput.h>

## Description

Gets the ValueInput object that defines the angle of the tip of the hole. The default is "118.0 deg" but can be modified by setting it using another Value object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeatureInput\_var" is a variable referencing a HoleFeatureInput object. |

"holeFeatureInput\_var" is a variable referencing a HoleFeatureInput object. ```` ``` #include <Fusion/Features/HoleFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = holeFeatureInput_var->tipAngle();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = holeFeatureInput_var->tipAngle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |