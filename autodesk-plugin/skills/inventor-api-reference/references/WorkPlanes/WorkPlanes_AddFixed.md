# WorkPlanes.AddFixed Method

Parent Object: [WorkPlanes](../WorkPlanes/WorkPlanes.md)

## Description

Method that creates a new work plane at the position and orientation defined by the point and X and Y axis vectors. When used to create a work plane within an assembly the resulting work plane will return an AssemblyWorkPlaneDef definition.

## Syntax

WorkPlanes.**AddFixed**( ***OriginPoint*** As [Point](../Point/Point.md), ***XAxis*** As [UnitVector](../UnitVector/UnitVector.md), ***YAxis*** As [UnitVector](../UnitVector/UnitVector.md), [***Construction***] As Boolean ) As [WorkPlane](../WorkPlane/WorkPlane.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| OriginPoint | [Point](../Point/Point.md) | Input Point object that defines the origin of the work plane. |
| XAxis | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector object that defines the X-axis vector of the work plane. |
| YAxis | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector object that defines the Y-axis vector of the work plane. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work plane as a construction plane or not. The default is False, which indicates to create a standard work plane, not a construction work plane. A construction work plane is hidden from the user and is not displayed graphically or listed in the browser. If work features are created as construction:  * Deleting any downstream feature that consumes this construction work feature will have the effect of deleting this work feature as well. * If there are no consumers of the construction work feature, it is the responsibility of the creator to delete them since they will never get cleaned up and are not visible to users. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |