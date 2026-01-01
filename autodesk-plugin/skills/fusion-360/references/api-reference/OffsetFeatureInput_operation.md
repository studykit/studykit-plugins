# OffsetFeatureInput.operation Property

Parent Object: [OffsetFeatureInput](OffsetFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeatureInput.h>

## Description

Gets and sets the feature operation to perform. Can be 'NewBodyFeatureOperation' or 'NewComponentFeatureOperation'.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFeatureInput\_var" is a variable referencing an OffsetFeatureInput object. |

"offsetFeatureInput\_var" is a variable referencing an OffsetFeatureInput object. ```` ``` #include <Fusion/Features/OffsetFeatureInput.h>  // Get the value of the property. FeatureOperations propertyValue = offsetFeatureInput_var->operation();  // Set the value of the property, where value_var is a FeatureOperations. bool returnValue = offsetFeatureInput_var->operation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [FeatureOperations](FeatureOperations.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |