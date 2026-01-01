# LoftFeatureInput.isValid Property

Parent Object: [LoftFeatureInput](LoftFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeatureInput.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeatureInput\_var" is a variable referencing a LoftFeatureInput object. |

"loftFeatureInput\_var" is a variable referencing a LoftFeatureInput object. ```` ``` #include <Fusion/Features/LoftFeatureInput.h>  // Get the value of the property. boolean propertyValue = loftFeatureInput_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |