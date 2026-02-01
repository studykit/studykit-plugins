# LoftFeatureInput.isTangentEdgesMerged Property

Parent Object: [LoftFeatureInput](LoftFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeatureInput.h>

## Description

Specifies if the loft will keep or merge tangent edges. These are edges between tangent faces in the resulting loft surface. If true, the faces will be merged so the connecting edge no longer exists

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeatureInput\_var" is a variable referencing a LoftFeatureInput object. |

"loftFeatureInput\_var" is a variable referencing a LoftFeatureInput object. ```` ``` #include <Fusion/Features/LoftFeatureInput.h>  // Get the value of the property. boolean propertyValue = loftFeatureInput_var->isTangentEdgesMerged();  // Set the value of the property, where value_var is a boolean. bool returnValue = loftFeatureInput_var->isTangentEdgesMerged(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |