# LoftFeatureInput.endLoftEdgeAlignment Property

Parent Object: [LoftFeatureInput](LoftFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeatureInput.h>

## Description

Specifies the end edge alignment option for the loft feature. The default is Free Edges.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeatureInput\_var" is a variable referencing a LoftFeatureInput object. |

"loftFeatureInput\_var" is a variable referencing a LoftFeatureInput object. ```` ``` #include <Fusion/Features/LoftFeatureInput.h>  // Get the value of the property. LoftEdgeAlignments propertyValue = loftFeatureInput_var->endLoftEdgeAlignment();  // Set the value of the property, where value_var is a LoftEdgeAlignments. bool returnValue = loftFeatureInput_var->endLoftEdgeAlignment(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [LoftEdgeAlignments](LoftEdgeAlignments.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |