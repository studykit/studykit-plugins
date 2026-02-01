# TemporaryBRepManager.createSilhouetteCurves Method

Parent Object: [TemporaryBRepManager](TemporaryBRepManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/TemporaryBRepManager.h>

## Description

Calculates the silhouette curve geometry for a given face as viewed from a given direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object.```` ``` returnValue = temporaryBRepManager_var.createSilhouetteCurves(face, viewDirection, returnCoincidentSilhouettes) ``` ```` |

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepBody](BRepBody.htm) | Returns a SurfaceBody object that will contain one or more BRepWire objects that represent the silhouette curve(s). This method can return null in the case where there is not a silhouette curve for the specified face. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| face | [BRepFace](BRepFace.htm) | Input BRepFace object to calculate the silhouette curve for. |
| viewDirection | [Vector3D](Vector3D.htm) | Input Vector3D object that defines the view direction to calculate the silhouette curve relative to. The silhouette curve(s) will lie along the path where the face normal is perpendicular to the view direction. |
| returnCoincidentSilhouettes | boolean | Input Boolean that specifies if silhouette curves that are coincident to the edges of the face should be returned or not. If true, these curves will be returned. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [TemporaryBRepManager API Sample](TemporaryBRepManager_Sample.htm) | TemporaryBRepManager related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |