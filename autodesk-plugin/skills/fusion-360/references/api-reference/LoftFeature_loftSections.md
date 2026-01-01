# LoftFeature.loftSections Property

Parent Object: [LoftFeature](LoftFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeature.h>

## Description

Returns the set of sections that the loft passes through.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeature\_var" is a variable referencing a LoftFeature object.  ```` ``` # Get the value of the property. propertyValue = loftFeature_var.loftSections ``` ```` |

"loftFeature\_var" is a variable referencing a LoftFeature object. ```` ``` #include <Fusion/Features/LoftFeature.h>  // Get the value of the property. Ptr<LoftSections> propertyValue = loftFeature_var->loftSections(); ``` ```` |

## Property Value

This is a read only property whose value is a [LoftSections](LoftSections.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |