# ScaleFeatureInput.scaleFactor Property

Parent Object: [ScaleFeatureInput](ScaleFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeatureInput.h>

## Description

Gets and sets the scale factor used for a uniform scale. Setting this value will cause the isUniform property to be set to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeatureInput\_var" is a variable referencing a ScaleFeatureInput object. |

"scaleFeatureInput\_var" is a variable referencing a ScaleFeatureInput object. ```` ``` #include <Fusion/Features/ScaleFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = scaleFeatureInput_var->scaleFactor();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = scaleFeatureInput_var->scaleFactor(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |