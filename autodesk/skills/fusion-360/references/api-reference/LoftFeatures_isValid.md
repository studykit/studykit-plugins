# LoftFeatures.isValid Property

Parent Object: [LoftFeatures](LoftFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeatures\_var" is a variable referencing a LoftFeatures object. |

"loftFeatures\_var" is a variable referencing a LoftFeatures object. ```` ``` #include <Fusion/Features/LoftFeatures.h>  // Get the value of the property. boolean propertyValue = loftFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |