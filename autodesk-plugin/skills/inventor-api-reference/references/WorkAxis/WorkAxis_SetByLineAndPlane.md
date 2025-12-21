# WorkAxis.SetByLineAndPlane Method

Parent Object: [WorkAxis](../WorkAxis/WorkAxis.md)

## Description

Method that redefines the work axis so that it is along a line defined by projecting the input line onto the input plane along the plane normal.

## Remarks

This method is not valid when the work axis exists in an Assembly component definition.

## Syntax

WorkAxis.**SetByLineAndPlane**( ***Line*** As Object, ***Plane*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Line | Object | Input object that represents a line. This object can be a linear Edge, WorkAxis, SketchLine, or SketchLine3D object. |
| Plane | Object | Input object that represents a plane. This object can be a planar Face, WorkPlane, or Sketch object. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |