# DeleteFaceFeatures.add Method

Parent Object: [DeleteFaceFeatures](DeleteFaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DeleteFaceFeatures.h>

## Description

Creates a new SurfaceDeleteFace feature. This deletes the specified faces from their bodies and attempts to heal the body. The method will fail if the body cannot be healed. This is equivalent to selecting and deleting faces when in the Patch workspace.

## Syntax

* [Python](#Python)
* [C++](#C++)

"deleteFaceFeatures\_var" is a variable referencing a [DeleteFaceFeatures](DeleteFaceFeatures.htm) object.```` ``` returnValue = deleteFaceFeatures_var.add(facesToDelete) ``` ```` |

"deleteFaceFeatures\_var" is a variable referencing a [DeleteFaceFeatures](DeleteFaceFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DeleteFaceFeature](DeleteFaceFeature.htm) | Returns the newly created DeleteFaceFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| facesToDelete | [Base](Base.htm) | A single BRepFace or an ObjectCollection containing multiple BRepFace objects. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |