# LinePlaneAndAngleWorkPlaneDef Object

## Description

Object that allows you to get and set the information that specifies a work plane that passes through a line and is a specified angle to a plane.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetData](../LinePlaneAndAngleWorkPlaneDef/LinePlaneAndAngleWorkPlaneDef_GetData.md) | Method that gets all of the data defining a work planed defined by a line, plane and an angle. The work plane passes through the line and is a specified angle to the plane. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Angle](../LinePlaneAndAngleWorkPlaneDef/LinePlaneAndAngleWorkPlaneDef_Angle.md) | Property that returns the parameter controlling the angle of a line, plane and angle defined work plane. The angle of the plane can be read and modified by accessing the returned Parameter object. The positive angle direction is computed by crossing the axis vector with the plane normal vector. Changes made will not be visible until the model is recomputed. |
| [Application](../LinePlaneAndAngleWorkPlaneDef/LinePlaneAndAngleWorkPlaneDef_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Line](../LinePlaneAndAngleWorkPlaneDef/LinePlaneAndAngleWorkPlaneDef_Line.md) | Property that returns the line of a line, plane and angle defined work plane. This object can be a linear Edge, WorkAxis, or SketchLine object. The work plane passes through the line. |
| [Parent](../LinePlaneAndAngleWorkPlaneDef/LinePlaneAndAngleWorkPlaneDef_Parent.md) | Property returning the parent WorkPlane object. |
| [Plane](../LinePlaneAndAngleWorkPlaneDef/LinePlaneAndAngleWorkPlaneDef_Plane.md) | Property that indicates the plane of a line, plane and angle defined work plane. This object can be a planar Face, WorkPlane, or Sketch object. The angle of the plane is measured with respect to this plane. |
| [Type](../LinePlaneAndAngleWorkPlaneDef/LinePlaneAndAngleWorkPlaneDef_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |