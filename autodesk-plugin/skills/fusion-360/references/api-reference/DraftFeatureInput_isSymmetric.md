# DraftFeatureInput.isSymmetric Property

Parent Object: [DraftFeatureInput](DraftFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeatureInput.h>

## Description

Gets if the draft is symmetric from the draft plane. This only applies in the case where two angles have been specified and should be ignored otherwise.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeatureInput\_var" is a variable referencing a DraftFeatureInput object. |

"draftFeatureInput\_var" is a variable referencing a DraftFeatureInput object. ```` ``` #include <Fusion/Features/DraftFeatureInput.h>  // Get the value of the property. boolean propertyValue = draftFeatureInput_var->isSymmetric(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |