# HoleFeatures.isValid Property

Parent Object: [HoleFeatures](HoleFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeatures\_var" is a variable referencing a HoleFeatures object. |

"holeFeatures\_var" is a variable referencing a HoleFeatures object. ```` ``` #include <Fusion/Features/HoleFeatures.h>  // Get the value of the property. boolean propertyValue = holeFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |