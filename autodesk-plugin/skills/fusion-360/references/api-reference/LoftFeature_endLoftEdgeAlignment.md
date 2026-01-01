# LoftFeature.endLoftEdgeAlignment Property

Parent Object: [LoftFeature](LoftFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeature.h>

## Description

Specifies the end edge alignment option for the loft feature. The default is Free Edges.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeature\_var" is a variable referencing a LoftFeature object. |

"loftFeature\_var" is a variable referencing a LoftFeature object. ```` ``` #include <Fusion/Features/LoftFeature.h>  // Get the value of the property. LoftEdgeAlignments propertyValue = loftFeature_var->endLoftEdgeAlignment();  // Set the value of the property, where value_var is a LoftEdgeAlignments. bool returnValue = loftFeature_var->endLoftEdgeAlignment(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [LoftEdgeAlignments](LoftEdgeAlignments.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |