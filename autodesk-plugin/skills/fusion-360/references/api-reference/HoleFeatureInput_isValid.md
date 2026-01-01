# HoleFeatureInput.isValid Property

Parent Object: [HoleFeatureInput](HoleFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeatureInput.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeatureInput\_var" is a variable referencing a HoleFeatureInput object. |

"holeFeatureInput\_var" is a variable referencing a HoleFeatureInput object. ```` ``` #include <Fusion/Features/HoleFeatureInput.h>  // Get the value of the property. boolean propertyValue = holeFeatureInput_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |