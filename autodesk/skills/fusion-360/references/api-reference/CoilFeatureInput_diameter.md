# CoilFeatureInput.diameter Property

Parent Object: [CoilFeatureInput](CoilFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CoilFeatureInput.h>

## Description

Gets and sets the diameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coilFeatureInput\_var" is a variable referencing a CoilFeatureInput object. |

"coilFeatureInput\_var" is a variable referencing a CoilFeatureInput object. ```` ``` #include <Fusion/Features/CoilFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = coilFeatureInput_var->diameter();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = coilFeatureInput_var->diameter(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |