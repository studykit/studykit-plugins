# HoleFeatureInput.isDefaultDirection Property

Parent Object: [HoleFeatureInput](HoleFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeatureInput.h>

## Description

Gets or sets if the hole goes in the default direction or is reversed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeatureInput\_var" is a variable referencing a HoleFeatureInput object. |

"holeFeatureInput\_var" is a variable referencing a HoleFeatureInput object. ```` ``` #include <Fusion/Features/HoleFeatureInput.h>  // Get the value of the property. boolean propertyValue = holeFeatureInput_var->isDefaultDirection();  // Set the value of the property, where value_var is a boolean. bool returnValue = holeFeatureInput_var->isDefaultDirection(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |