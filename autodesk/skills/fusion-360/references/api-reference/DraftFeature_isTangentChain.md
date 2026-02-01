# DraftFeature.isTangentChain Property

Parent Object: [DraftFeature](DraftFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeature.h>

## Description

Gets and sets if any faces that are tangentially connected to any of the input faces will also be included in setting InputEntities. It defaults to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeature\_var" is a variable referencing a DraftFeature object.  ```` ``` # Get the value of the property. propertyValue = draftFeature_var.isTangentChain  # Set the value of the property. draftFeature_var.isTangentChain = propertyValue ``` ```` |

"draftFeature\_var" is a variable referencing a DraftFeature object. ```` ``` #include <Fusion/Features/DraftFeature.h>  // Get the value of the property. boolean propertyValue = draftFeature_var->isTangentChain();  // Set the value of the property, where value_var is a boolean. bool returnValue = draftFeature_var->isTangentChain(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |