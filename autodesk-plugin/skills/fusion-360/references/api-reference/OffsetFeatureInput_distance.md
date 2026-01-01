# OffsetFeatureInput.distance Property

Parent Object: [OffsetFeatureInput](OffsetFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeatureInput.h>

## Description

Gets and sets the ValueInput object that defines the offset distance. A positive distance value results in an offset in the positive normal direction of the faces.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFeatureInput\_var" is a variable referencing an OffsetFeatureInput object. |

"offsetFeatureInput\_var" is a variable referencing an OffsetFeatureInput object. ```` ``` #include <Fusion/Features/OffsetFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = offsetFeatureInput_var->distance();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = offsetFeatureInput_var->distance(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |