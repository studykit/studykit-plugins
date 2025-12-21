# WorkPoint.SetByThreePlanes Method

Parent Object: [WorkPoint](../WorkPoint/WorkPoint.md)

## Description

Method that redefines the work point to be at the intersection of the three input planes.

## Remarks

If the three input planes don't intersect an error will occur. This method is not valid when the work point exists in an Assembly component definition.

## Syntax

WorkPoint.**SetByThreePlanes**( ***Plane1*** As Object, ***Plane2*** As Object, ***Plane3*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Plane1 | Object | Input object that represents a plane. This object can be a planar Face, WorkPlane, or Sketch object. |
| Plane2 | Object | Input object that represents a plane. This object can be a planar Face, WorkPlane, or Sketch object. |
| Plane3 | Object | Input object that represents a plane. This object can be a planar Face, WorkPlane, or Sketch object. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |