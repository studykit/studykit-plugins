# SurfaceDeleteFaceFeatures.add Method

Parent Object: [SurfaceDeleteFaceFeatures](SurfaceDeleteFaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SurfaceDeleteFaceFeatures.h>

## Description

Creates a new SurfaceDeleteFaceFeature feature. This deletes the specified faces from their bodies without any attempt to heal the openings. This is equivalent to selecting and deleting faces when in the Patch workspace.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceDeleteFaceFeatures\_var" is a variable referencing a [SurfaceDeleteFaceFeatures](SurfaceDeleteFaceFeatures.htm) object.```` ``` returnValue = surfaceDeleteFaceFeatures_var.add(facesToDelete) ``` ```` |

"surfaceDeleteFaceFeatures\_var" is a variable referencing a [SurfaceDeleteFaceFeatures](SurfaceDeleteFaceFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm) | Returns the newly created SurfaceDeleteFaceFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| facesToDelete | [Base](Base.htm) | A single BRepFace or an ObjectCollection containing multiple BRepFace objects. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [DeleteFace Feature API Sample](DeleteFaceFeatureSample_Sample.htm) | Demonstrates creating a new deleteFace feature. |
| [surfaceDeleteFeatures.add](surfaceDeleteFeatures_add_Sample.htm) | Demonstrates the surfaceDeleteFeatures.add method. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |