# WorkPoints.AddByTwoLines Method

Parent Object: [WorkPoints](../WorkPoints/WorkPoints.md)

## Description

Method that creates a new work point at the intersection of the two input lines. If the lines don't intersect an error will occur. This method is not currently supported when creating a work point within an assembly.

## Syntax

WorkPoints.**AddByTwoLines**( ***Line1*** As Object, ***Line2*** As Object, [***Construction***] As Boolean ) As [WorkPoint](../WorkPoint/WorkPoint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Line1 | Object | Input object that represents a line. This object can be a linear Edge, WorkAxis, or SketchLine object. |
| Line2 | Object | Input object that represents a line. This object can be a linear Edge, WorkAxis, or SketchLine object. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work point as a construction point or not. The default is False, which indicates to create a standard work point. A construction work point is hidden from the user and is not displayed graphically or listed in the browser. If work features are created as construction:  * Deleting any downstream feature that consumes this construction work feature will have the effect of deleting this work feature as well. * If there are no consumers of the construction work feature, it is the responsibility of the creator to delete them since they will never get cleaned up and are not visible to users. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |