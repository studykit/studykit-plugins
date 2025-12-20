# MoveFaceDefinition.SetPlanarMoveType Method

Parent Object: [MoveFaceDefinition](../MoveFaceDefinition/MoveFaceDefinition.md)

## Description

Method that sets the move face type to kPlanarMoveType. The move is defined using two points, and optionally, a plane for the move.

## Syntax

MoveFaceDefinition.**SetPlanarMoveType**( ***PointOne*** As Object, ***PointTwo*** As Object, [***Plane***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PointOne | Object | Specifies the first point for the planar move. This can either be a WorkPoint or a Vertex object. |
| PointTwo | Object | Specifies the second point for the planar move. This can either be a WorkPoint or a Vertex object. |
| Plane | Variant | Specifies the plane for the planar move. This can either be a WorkPlane or a planar Face object. If not specified, the move is based on the input points. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |