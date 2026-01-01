# LoftFeature.isSolid Property

Parent Object: [LoftFeature](LoftFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeature.h>

## Description

Indicates if this feature was initially created as a solid or a surface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeature\_var" is a variable referencing a LoftFeature object. |

"loftFeature\_var" is a variable referencing a LoftFeature object. ```` ``` #include <Fusion/Features/LoftFeature.h>  // Get the value of the property. boolean propertyValue = loftFeature_var->isSolid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |