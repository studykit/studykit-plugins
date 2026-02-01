# PatchFeatureInput.groupWeight Property

Parent Object: [PatchFeatureInput](PatchFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeatureInput.h>

## Description

Gets and sets the weight to use for all edges when the isGroupEdges property is true. It is ignored for any sketch curves in the boundary. The property defaults to 0.5. The value of this property is ignored if the isGroupEdges property is false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeatureInput\_var" is a variable referencing a PatchFeatureInput object. |

"patchFeatureInput\_var" is a variable referencing a PatchFeatureInput object. ```` ``` #include <Fusion/Features/PatchFeatureInput.h>  // Get the value of the property. double propertyValue = patchFeatureInput_var->groupWeight();  // Set the value of the property, where value_var is a double. bool returnValue = patchFeatureInput_var->groupWeight(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |