# ScaleFeatures.isValid Property

Parent Object: [ScaleFeatures](ScaleFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeatures\_var" is a variable referencing a ScaleFeatures object. |

"scaleFeatures\_var" is a variable referencing a ScaleFeatures object. ```` ``` #include <Fusion/Features/ScaleFeatures.h>  // Get the value of the property. boolean propertyValue = scaleFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |