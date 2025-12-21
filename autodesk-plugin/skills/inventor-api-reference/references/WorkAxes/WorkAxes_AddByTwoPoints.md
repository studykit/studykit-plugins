# WorkAxes.AddByTwoPoints Method

Parent Object: [WorkAxes](../WorkAxes/WorkAxes.md)

## Description

Method that creates a new work axis through the two input points. This method is not currently supported when creating a work axis within an assembly.

## Syntax

WorkAxes.**AddByTwoPoints**( ***Point1*** As Object, ***Point2*** As Object, [***Construction***] As Boolean ) As [WorkAxis](../WorkAxis/WorkAxis.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point1 | Object | Input object that represents a point. This object can be a WorkPoint, Vertex, or SketchPoint object. |
| Point2 | Object | Input object that represents a point. This object can be a WorkPoint, Vertex, or SketchPoint object. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work axis as a construction axis or not. The default is False, which indicates to create a standard work axis, not a construction work axis. A construction work axis is hidden from the user and is not displayed graphically or listed in the browser. If work features are created as construction: \* Deleting any downstream feature that consumes this construction work feature will have the effect of deleting this work feature as well. \* If there are no consumers of the construction work feature, it is the responsibility of the creator to delete them since they will never get cleaned up and are not visible to users. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |