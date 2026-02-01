# ChamferFeatureInput.cornerType Property

Parent Object: [ChamferFeatureInput](ChamferFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeatureInput.h>

## Description

Gets and sets the type of corner to be modeled when multiple edges connect at a vertex.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeatureInput\_var" is a variable referencing a ChamferFeatureInput object. |

"chamferFeatureInput\_var" is a variable referencing a ChamferFeatureInput object. ```` ``` #include <Fusion/Features/ChamferFeatureInput.h>  // Get the value of the property. ChamferCornerTypes propertyValue = chamferFeatureInput_var->cornerType();  // Set the value of the property, where value_var is a ChamferCornerTypes. bool returnValue = chamferFeatureInput_var->cornerType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ChamferCornerTypes](ChamferCornerTypes.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |