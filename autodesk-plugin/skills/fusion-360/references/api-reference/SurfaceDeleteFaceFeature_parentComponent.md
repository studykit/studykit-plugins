# SurfaceDeleteFaceFeature.parentComponent Property

Parent Object: [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SurfaceDeleteFaceFeature.h>

## Description

Returns the parent component that owns this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceDeleteFaceFeature\_var" is a variable referencing a SurfaceDeleteFaceFeature object. |

"surfaceDeleteFaceFeature\_var" is a variable referencing a SurfaceDeleteFaceFeature object. ```` ``` #include <Fusion/Features/SurfaceDeleteFaceFeature.h>  // Get the value of the property. Ptr<Component> propertyValue = surfaceDeleteFaceFeature_var->parentComponent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |