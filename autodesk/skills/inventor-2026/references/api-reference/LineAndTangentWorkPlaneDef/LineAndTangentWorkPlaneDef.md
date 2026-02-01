# LineAndTangentWorkPlaneDef Object

## Description

Object that allows you to get and set the information that specifies a work plane that passes through a line and is tangent to a surface.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetData](../LineAndTangentWorkPlaneDef/LineAndTangentWorkPlaneDef_GetData.md) | Method that gets all of the data defining a work that passes through the line and is tangent to the input face. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../LineAndTangentWorkPlaneDef/LineAndTangentWorkPlaneDef_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Face](../LineAndTangentWorkPlaneDef/LineAndTangentWorkPlaneDef_Face.md) | Property that returns the tangent of the work plane. This face must either be a cylinder whose axis is parallel to the line, a cone that is positioned such that a valid tangent exists, or a sphere. |
| [Line](../LineAndTangentWorkPlaneDef/LineAndTangentWorkPlaneDef_Line.md) | Property that returns the line of a work plane that passes through a line and is tangent to a surface. This object can be a linear Edge, WorkAxis, or SketchLine object. |
| [Parent](../LineAndTangentWorkPlaneDef/LineAndTangentWorkPlaneDef_Parent.md) | Property returning the parent WorkPlane object. |
| [ProximityPoint](../LineAndTangentWorkPlaneDef/LineAndTangentWorkPlaneDef_ProximityPoint.md) | Property that returns the proximity point. The proximity point defines which of the two possible solutions is chosen when computing the tangent plane. This point is used for the initial computation and the specific point is not stored. During a recompute of the model the plane will remain on the same side of the tangent surface regardless of its position relative to the originally specified point. The point returned by this property is as an arbitrary point along the tangent between the face and plane. |
| [Type](../LineAndTangentWorkPlaneDef/LineAndTangentWorkPlaneDef_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 4
