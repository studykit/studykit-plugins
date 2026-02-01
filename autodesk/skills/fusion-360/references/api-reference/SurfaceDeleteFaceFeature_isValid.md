# SurfaceDeleteFaceFeature.isValid Property

Parent Object: [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SurfaceDeleteFaceFeature.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceDeleteFaceFeature\_var" is a variable referencing a SurfaceDeleteFaceFeature object. |

"surfaceDeleteFaceFeature\_var" is a variable referencing a SurfaceDeleteFaceFeature object. ```` ``` #include <Fusion/Features/SurfaceDeleteFaceFeature.h>  // Get the value of the property. boolean propertyValue = surfaceDeleteFaceFeature_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |