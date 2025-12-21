# PlaneAndTangentWorkPlaneDef Object

## Description

Object that allows you to get and set the information that specifies a work plane that is parallel to a plane and tangent to a surface.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetData](../PlaneAndTangentWorkPlaneDef/PlaneAndTangentWorkPlaneDef_GetData.md) | Method that gets all of the data defining a work that is parallel to the plane and tangent to the input face. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PlaneAndTangentWorkPlaneDef/PlaneAndTangentWorkPlaneDef_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Face](../PlaneAndTangentWorkPlaneDef/PlaneAndTangentWorkPlaneDef_Face.md) | Property that returns the tangent of the work plane. This face must either be a cylinder whose axis is parallel to the line, a cone that is positioned such that a valid tangent exists, or a sphere. |
| [Parent](../PlaneAndTangentWorkPlaneDef/PlaneAndTangentWorkPlaneDef_Parent.md) | Property returning the parent WorkPlane object. |
| [Plane](../PlaneAndTangentWorkPlaneDef/PlaneAndTangentWorkPlaneDef_Plane.md) | Property that returns the plane of a work plane that is parallel to a plane and tangent to a surface. This object can be a planar Face, WorkPlane, or Sketch object. The work plane will be parallel to this plane. |
| [ProximityPoint](../PlaneAndTangentWorkPlaneDef/PlaneAndTangentWorkPlaneDef_ProximityPoint.md) | Property that returns the proximity point. The proximity point defines which of the two possible solutions is chosen when computing the tangent plane. This point is used for the initial computation and the specific point is not stored. During a recompute of the model the plane will remain on the same side of the tangent surface regardless of its position relative to the originally specified point. The point returned by this property is as an arbitrary point along the tangent between the face and plane. |
| [Type](../PlaneAndTangentWorkPlaneDef/PlaneAndTangentWorkPlaneDef_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |