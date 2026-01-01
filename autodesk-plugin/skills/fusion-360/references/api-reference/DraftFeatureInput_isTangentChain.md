# DraftFeatureInput.isTangentChain Property

Parent Object: [DraftFeatureInput](DraftFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeatureInput.h>

## Description

Gets and sets if any faces that are tangentially connected to any of the input faces will also be included in setting InputEntities. It defaults to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeatureInput\_var" is a variable referencing a DraftFeatureInput object. |

"draftFeatureInput\_var" is a variable referencing a DraftFeatureInput object. ```` ``` #include <Fusion/Features/DraftFeatureInput.h>  // Get the value of the property. boolean propertyValue = draftFeatureInput_var->isTangentChain();  // Set the value of the property, where value_var is a boolean. bool returnValue = draftFeatureInput_var->isTangentChain(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |