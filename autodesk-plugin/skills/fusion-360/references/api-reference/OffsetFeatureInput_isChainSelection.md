# OffsetFeatureInput.isChainSelection Property

Parent Object: [OffsetFeatureInput](OffsetFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeatureInput.h>

## Description

Get and sets whether faces that are tangentially connected to the input faces will be included in the offset.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFeatureInput\_var" is a variable referencing an OffsetFeatureInput object. |

"offsetFeatureInput\_var" is a variable referencing an OffsetFeatureInput object. ```` ``` #include <Fusion/Features/OffsetFeatureInput.h>  // Get the value of the property. boolean propertyValue = offsetFeatureInput_var->isChainSelection();  // Set the value of the property, where value_var is a boolean. bool returnValue = offsetFeatureInput_var->isChainSelection(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |