# BoundaryFillFeature.nativeObject Property

Parent Object: [BoundaryFillFeature](BoundaryFillFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeature.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeature\_var" is a variable referencing a BoundaryFillFeature object. |

"boundaryFillFeature\_var" is a variable referencing a BoundaryFillFeature object. ```` ``` #include <Fusion/Features/BoundaryFillFeature.h>  // Get the value of the property. Ptr<BoundaryFillFeature> propertyValue = boundaryFillFeature_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [BoundaryFillFeature](BoundaryFillFeature.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |