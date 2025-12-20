# PointAndTangentWorkPlaneDef Object

## Description

Object that allows you to get and set the information that specifies a work plane that passes through a point and is tangent to a surface.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetData](../PointAndTangentWorkPlaneDef/PointAndTangentWorkPlaneDef_GetData.md) | Method that gets all of the data defining a work that passes through a point and is tangent to the input face. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PointAndTangentWorkPlaneDef/PointAndTangentWorkPlaneDef_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Face](../PointAndTangentWorkPlaneDef/PointAndTangentWorkPlaneDef_Face.md) | Property that returns the tangent face of the work plane. This face must either be a cylinder whose axis is parallel to the line, a cone that is positioned such that a valid tangent exists, a sphere or a bspline surface. |
| [Parent](../PointAndTangentWorkPlaneDef/PointAndTangentWorkPlaneDef_Parent.md) | Property that returns the parent WorkPlane object. |
| [Point](../PointAndTangentWorkPlaneDef/PointAndTangentWorkPlaneDef_Point.md) | Property that returns the point of a work plane that passes through a point and is tangent to a surface. This object can be a Vertex, WorkPoint, SketchPoint, or SketchPoint3D object. |
| [Type](../PointAndTangentWorkPlaneDef/PointAndTangentWorkPlaneDef_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |