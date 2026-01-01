# SurfaceDeleteFaceFeature.name Property

Parent Object: [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SurfaceDeleteFaceFeature.h>

## Description

Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric).

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceDeleteFaceFeature\_var" is a variable referencing a SurfaceDeleteFaceFeature object. |

"surfaceDeleteFaceFeature\_var" is a variable referencing a SurfaceDeleteFaceFeature object. ```` ``` #include <Fusion/Features/SurfaceDeleteFaceFeature.h>  // Get the value of the property. string propertyValue = surfaceDeleteFaceFeature_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = surfaceDeleteFaceFeature_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |