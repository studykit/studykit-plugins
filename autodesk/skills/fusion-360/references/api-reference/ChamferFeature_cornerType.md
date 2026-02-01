# ChamferFeature.cornerType Property

Parent Object: [ChamferFeature](ChamferFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeature.h>

## Description

Gets and sets the type of corner to be modeled when multiple edges connect at a vertex.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeature\_var" is a variable referencing a ChamferFeature object. |

"chamferFeature\_var" is a variable referencing a ChamferFeature object. ```` ``` #include <Fusion/Features/ChamferFeature.h>  // Get the value of the property. ChamferCornerTypes propertyValue = chamferFeature_var->cornerType();  // Set the value of the property, where value_var is a ChamferCornerTypes. bool returnValue = chamferFeature_var->cornerType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ChamferCornerTypes](ChamferCornerTypes.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |