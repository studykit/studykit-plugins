# WorkPlanes.AddByTwoLines Method

Parent Object: [WorkPlanes](../WorkPlanes/WorkPlanes.md)

## Description

Method that creates a new work plane based on the two input lines. Line1 defines the X axis. If the two lines are not in the same plane, the plane is calculated by crossing the vectors defined by Line1 and Line2. This method is not currently supported when creating a work plane within an assembly.

## Syntax

WorkPlanes.**AddByTwoLines**( ***Line1*** As Object, ***Line2*** As Object, [***Construction***] As Boolean ) As [WorkPlane](../WorkPlane/WorkPlane.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Line1 | Object | Input object that represents a line. This object can be a linear Edge, WorkAxis, or SketchLine object. |
| Line2 | Object | Input object that represents a line. This object can be a linear Edge, WorkAxis, or SketchLine object. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work plane as a construction plane or not. The default is False, which indicates to create a standard work plane, not a construction work plane. A construction work plane is hidden from the user and is not displayed graphically or listed in the browser. If work features are created as construction: \*  * Deleting any downstream feature that consumes this construction work feature will have the effect of deleting this work feature as well. * If there are no consumers of the construction work feature, it is the responsibility of the creator to delete them since they will never get cleaned up and are not visible to users. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |