# PlaneAndOffsetWorkPlaneDef Object

## Description

Object that allows you to get and set the information that specifies a work plane that is parallel to an existing plane and offset a specified distance.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetData](../PlaneAndOffsetWorkPlaneDef/PlaneAndOffsetWorkPlaneDef_GetData.md) | Method that gets all of the data defining a work planed defined by a plane, direction and offset. The work plane is parallel to the plane and is offset the specified distance in the specified direction. The sign of the value controls which side of the plane the offset is in. A positive value will be in the positive normal side of the plane. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PlaneAndOffsetWorkPlaneDef/PlaneAndOffsetWorkPlaneDef_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Offset](../PlaneAndOffsetWorkPlaneDef/PlaneAndOffsetWorkPlaneDef_Offset.md) | Property that returns the parameter controlling the offset of the work plane. The offset of the plane can be read and modified by accessing the returned Parameter object. |
| [Parent](../PlaneAndOffsetWorkPlaneDef/PlaneAndOffsetWorkPlaneDef_Parent.md) | Property returning the parent WorkPlane object. |
| [Plane](../PlaneAndOffsetWorkPlaneDef/PlaneAndOffsetWorkPlaneDef_Plane.md) | Property that returns the plane of an offset work plane. This object can be a planar Face, WorkPlane, or Sketch object. The work plane will be parallel to this plane. |
| [Type](../PlaneAndOffsetWorkPlaneDef/PlaneAndOffsetWorkPlaneDef_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |