# DraftFeature.draftDefinition Property

Parent Object: [DraftFeature](DraftFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeature.h>

## Description

Gets the definition object that specifies how the draft is defined. Modifying the definition object will cause the draft to recompute. This can return either an AngleExtentDefinition or TwoSidesAngleExtentDefinition object. This property returns nothing in the case where the feature is non-parametric. Use this property to access the parameters controlling the draft and whether the draft is symmetric or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeature\_var" is a variable referencing a DraftFeature object. |

"draftFeature\_var" is a variable referencing a DraftFeature object. ```` ``` #include <Fusion/Features/DraftFeature.h>  // Get the value of the property. Ptr<ExtentDefinition> propertyValue = draftFeature_var->draftDefinition(); ``` ```` |

## Property Value

This is a read only property whose value is an [ExtentDefinition](ExtentDefinition.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |