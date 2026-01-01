# SurfaceDeleteFaceFeature.dissolve Method

Parent Object: [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SurfaceDeleteFaceFeature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceDeleteFaceFeature\_var" is a variable referencing a [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm) object.```` ``` returnValue = surfaceDeleteFaceFeature_var.dissolve() ``` ```` |

"surfaceDeleteFaceFeature\_var" is a variable referencing a [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns a bool indicating if the dissolve was successful or not. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |