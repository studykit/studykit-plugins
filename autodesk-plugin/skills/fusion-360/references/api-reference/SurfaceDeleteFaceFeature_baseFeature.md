# SurfaceDeleteFaceFeature.baseFeature Property

Parent Object: [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SurfaceDeleteFaceFeature.h>

## Description

If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceDeleteFaceFeature\_var" is a variable referencing a SurfaceDeleteFaceFeature object. |

"surfaceDeleteFaceFeature\_var" is a variable referencing a SurfaceDeleteFaceFeature object. ```` ``` #include <Fusion/Features/SurfaceDeleteFaceFeature.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = surfaceDeleteFaceFeature_var->baseFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |