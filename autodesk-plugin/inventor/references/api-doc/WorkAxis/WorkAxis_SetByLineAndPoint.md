# WorkAxis.SetByLineAndPoint Method

Parent Object: [WorkAxis](../WorkAxis/WorkAxis.md)

## Description

Method that redefines the work axis so that it is parallel to a line and passes through the input point.

## Remarks

This method is not valid when the work axis exists in an Assembly component definition.

## Syntax

WorkAxis.**SetByLineAndPoint**( ***Line*** As Object, ***Point*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Line | Object | Input object that represents a line. This object can be a linear Edge, WorkAxis, SketchLine, or SketchLine3D object. |
| Point | Object | Input object that represents a point. This object can be a Vertex, WorkPoint, SketchPoint, or SketchPoint3D object. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |