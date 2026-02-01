# UntrimFeatureInput.extensionDistance Property

Parent Object: [UntrimFeatureInput](UntrimFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeatureInput.h>

## Description

Gets and sets the ValueInput object that defines the extension distance applied to faces when an external boundary is removed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"untrimFeatureInput\_var" is a variable referencing a UntrimFeatureInput object. |

"untrimFeatureInput\_var" is a variable referencing a UntrimFeatureInput object. ```` ``` #include <Fusion/Features/UntrimFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = untrimFeatureInput_var->extensionDistance();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = untrimFeatureInput_var->extensionDistance(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |