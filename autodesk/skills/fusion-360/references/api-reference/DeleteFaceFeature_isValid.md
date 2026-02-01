# DeleteFaceFeature.isValid Property

Parent Object: [DeleteFaceFeature](DeleteFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DeleteFaceFeature.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"deleteFaceFeature\_var" is a variable referencing a DeleteFaceFeature object. |

"deleteFaceFeature\_var" is a variable referencing a DeleteFaceFeature object. ```` ``` #include <Fusion/Features/DeleteFaceFeature.h>  // Get the value of the property. boolean propertyValue = deleteFaceFeature_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |