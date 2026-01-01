# SurfaceDeleteFaceFeature.isSuppressed Property

Parent Object: [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SurfaceDeleteFaceFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceDeleteFaceFeature\_var" is a variable referencing a SurfaceDeleteFaceFeature object. |

"surfaceDeleteFaceFeature\_var" is a variable referencing a SurfaceDeleteFaceFeature object. ```` ``` #include <Fusion/Features/SurfaceDeleteFaceFeature.h>  // Get the value of the property. boolean propertyValue = surfaceDeleteFaceFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = surfaceDeleteFaceFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |