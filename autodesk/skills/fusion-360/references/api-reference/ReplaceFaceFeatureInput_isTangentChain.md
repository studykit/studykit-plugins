# ReplaceFaceFeatureInput.isTangentChain Property

Parent Object: [ReplaceFaceFeatureInput](ReplaceFaceFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReplaceFaceFeatureInput.h>

## Description

Gets and sets if any faces that are tangentially connected to any of the input faces will also be included in setting InputEntities. It defaults to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"replaceFaceFeatureInput\_var" is a variable referencing a ReplaceFaceFeatureInput object. |

"replaceFaceFeatureInput\_var" is a variable referencing a ReplaceFaceFeatureInput object. ```` ``` #include <Fusion/Features/ReplaceFaceFeatureInput.h>  // Get the value of the property. boolean propertyValue = replaceFaceFeatureInput_var->isTangentChain();  // Set the value of the property, where value_var is a boolean. bool returnValue = replaceFaceFeatureInput_var->isTangentChain(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |