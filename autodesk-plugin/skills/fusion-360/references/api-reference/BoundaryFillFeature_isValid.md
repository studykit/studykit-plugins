# BoundaryFillFeature.isValid Property

Parent Object: [BoundaryFillFeature](BoundaryFillFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeature.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeature\_var" is a variable referencing a BoundaryFillFeature object. |

"boundaryFillFeature\_var" is a variable referencing a BoundaryFillFeature object. ```` ``` #include <Fusion/Features/BoundaryFillFeature.h>  // Get the value of the property. boolean propertyValue = boundaryFillFeature_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |