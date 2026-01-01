# LoftFeature.name Property

Parent Object: [LoftFeature](LoftFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeature.h>

## Description

Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric).

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeature\_var" is a variable referencing a LoftFeature object. |

"loftFeature\_var" is a variable referencing a LoftFeature object. ```` ``` #include <Fusion/Features/LoftFeature.h>  // Get the value of the property. string propertyValue = loftFeature_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = loftFeature_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |