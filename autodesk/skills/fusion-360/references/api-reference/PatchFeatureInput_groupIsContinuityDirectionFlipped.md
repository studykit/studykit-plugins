# PatchFeatureInput.groupIsContinuityDirectionFlipped Property

Parent Object: [PatchFeatureInput](PatchFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeatureInput.h>

## Description

Gets and sets the continuity direction for all edges when the isGroupEdges property is true. It is ignored for any sketch curves in the boundary. The property defaults to false. The value of this property is ignored if the isGroupEdges property is false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeatureInput\_var" is a variable referencing a PatchFeatureInput object. |

"patchFeatureInput\_var" is a variable referencing a PatchFeatureInput object. ```` ``` #include <Fusion/Features/PatchFeatureInput.h>  // Get the value of the property. boolean propertyValue = patchFeatureInput_var->groupIsContinuityDirectionFlipped();  // Set the value of the property, where value_var is a boolean. bool returnValue = patchFeatureInput_var->groupIsContinuityDirectionFlipped(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |